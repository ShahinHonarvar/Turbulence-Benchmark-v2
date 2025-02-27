def palindromes_between_indices(s):
    substring = s[2:5]
    letters = [c.lower() for c in substring if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, prefix='', length=4):
        if len(prefix) == length:
            if is_palindrome(prefix):
                palindromes.add(prefix)
            return
        for char in chars:
            generate_palindromes(chars, prefix + char, length)
    generate_palindromes(letters)
    return palindromes