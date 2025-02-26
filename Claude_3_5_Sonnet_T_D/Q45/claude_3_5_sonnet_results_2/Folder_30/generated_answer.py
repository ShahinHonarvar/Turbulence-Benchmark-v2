def palindromes_between_indices(s):
    letters = ''.join((c for c in s[:5] if c.isalpha())).lower()
    result = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and is_palindrome(current):
            result.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result