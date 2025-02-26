def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, prefix=''):
        if len(prefix) >= 4 and is_palindrome(prefix):
            palindromes.add(prefix)
        if chars:
            for i in range(len(chars)):
                generate_palindromes(chars[:i] + chars[i + 1:], prefix + chars[i])
    palindromes = set()
    generate_palindromes(letters)
    return palindromes