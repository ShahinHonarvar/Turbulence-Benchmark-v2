def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:9] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 4

    def generate_palindromes(chars, current=''):
        if len(current) >= 4 and is_palindrome(current):
            palindromes.add(current)
        for i in range(len(chars)):
            generate_palindromes(chars[:i] + chars[i + 1:], current + chars[i])
    palindromes = set()
    generate_palindromes(letters)
    return palindromes