def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[8:10] if c.isalpha()))
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                result.add(current)
        if len(remaining) > 0:
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
                generate_palindromes(char + current, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', ''.join(letters))
    return result