def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, prefix=''):
        if len(prefix) >= 5 and is_palindrome(prefix):
            palindromes.add(prefix)
        for i in range(len(chars)):
            generate_palindromes(chars[:i] + chars[i + 1:], prefix + chars[i])
    generate_palindromes(letters)
    return palindromes