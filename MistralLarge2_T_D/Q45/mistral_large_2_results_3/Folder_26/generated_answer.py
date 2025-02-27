def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, prefix='', length=3):
        if length == 0 and is_palindrome(prefix):
            palindromes.add(prefix)
        elif length > 0:
            for char in chars:
                generate_palindromes(chars, prefix + char, length - 1)
    generate_palindromes(letters)
    return palindromes