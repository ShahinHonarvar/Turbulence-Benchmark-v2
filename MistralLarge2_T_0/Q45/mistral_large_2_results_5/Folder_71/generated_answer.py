def palindromes_between_indices(s):
    substring = s[1:4].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', length=4):
        if len(current) == length:
            if is_palindrome(current):
                palindromes.add(current)
            return
        for letter in letters:
            generate_palindromes(letters, current + letter, length)
    for length in range(4, len(letters) + 1):
        generate_palindromes(letters, length=length)
    return palindromes