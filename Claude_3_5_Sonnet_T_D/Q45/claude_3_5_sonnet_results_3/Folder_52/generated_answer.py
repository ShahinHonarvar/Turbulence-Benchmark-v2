def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    n = len(letters)
    result = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 6 and is_palindrome(current):
            result.add(current)
        if len(current) < n:
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result