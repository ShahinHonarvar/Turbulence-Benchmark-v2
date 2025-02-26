def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[:6] if c.isalpha()))
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 5:
            palindromes.add(current)
        if len(remaining) > 0:
            for i, char in enumerate(remaining):
                generate_palindromes(char + current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', ''.join(letters))
    return palindromes