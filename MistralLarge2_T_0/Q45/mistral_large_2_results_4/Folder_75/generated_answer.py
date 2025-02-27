def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', length=3):
        if length == 0:
            if is_palindrome(current):
                palindromes.add(current)
            return
        for letter in letters:
            generate_palindromes(letters, current + letter, length - 1)
    for length in range(3, len(letters) + 1):
        generate_palindromes(letters, length=length)
    return palindromes