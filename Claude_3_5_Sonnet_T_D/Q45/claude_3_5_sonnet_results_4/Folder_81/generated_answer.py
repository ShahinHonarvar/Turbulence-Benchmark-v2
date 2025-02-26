def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[:7] if c.isalpha()))
    result = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and is_palindrome(current):
            result.add(current)
        if len(current) < len(letters):
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result