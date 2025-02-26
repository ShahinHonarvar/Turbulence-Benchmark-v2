def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 6 and is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes