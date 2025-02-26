def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:3] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3

    def generate_palindromes(chars, current='', remaining=None):
        if remaining is None:
            remaining = chars
        if is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(chars, current + char, remaining[:i] + remaining[i + 1:])
    palindromes = set()
    generate_palindromes(letters)
    return palindromes