def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, prefix=''):
        if len(prefix) >= 4 and is_palindrome(prefix):
            palindromes.add(prefix)
        if len(chars) > 0:
            for i in range(len(chars)):
                generate_palindromes(chars[:i] + chars[i + 1:], prefix + chars[i])
    generate_palindromes(letters)
    return palindromes