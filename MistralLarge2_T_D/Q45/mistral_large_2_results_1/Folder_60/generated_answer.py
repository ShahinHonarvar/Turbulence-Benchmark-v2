def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', length=4):
        if length == 0 and is_palindrome(current):
            palindromes.add(current)
            return
        if length < 0 or not letters:
            return
        for i, letter in enumerate(letters):
            generate_palindromes(letters[:i] + letters[i + 1:], current + letter, length - 1)
    for length in range(4, len(letters) + 1):
        generate_palindromes(letters, '', length)
    return palindromes