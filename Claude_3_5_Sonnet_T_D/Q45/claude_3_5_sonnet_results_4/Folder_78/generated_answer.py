def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:9] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3

    def generate_palindromes(chars, current=''):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes