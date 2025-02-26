def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    result = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 5 and is_palindrome(current):
            result.add(current)
        if len(current) < 10:
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result