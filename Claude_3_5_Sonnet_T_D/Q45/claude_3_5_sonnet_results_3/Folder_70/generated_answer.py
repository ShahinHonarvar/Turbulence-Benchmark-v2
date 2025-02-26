def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current='', length=0):
        if length >= 4:
            if is_palindrome(current):
                palindromes.add(current)
        if chars:
            for i, char in enumerate(chars):
                generate_palindromes(chars[:i] + chars[i + 1:], current + char, length + 1)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes