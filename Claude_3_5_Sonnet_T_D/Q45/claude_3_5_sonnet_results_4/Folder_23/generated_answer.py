def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and is_palindrome(current):
            palindromes.add(current)
        if len(current) < len(letters):
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', ''.join(letters))
    return palindromes