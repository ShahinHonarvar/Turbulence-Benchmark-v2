def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:8] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes