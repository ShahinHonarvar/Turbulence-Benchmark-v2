def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[7:10] if c.isalpha()))
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(current) == len(remaining) * 2 - (1 if len(current) % 2 else 0):
            palindromes.add(current)
            return
        for i in range(len(remaining)):
            char = remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(current + char, new_remaining)
            if len(current) > 0:
                generate_palindromes(char + current, new_remaining)
    if not letters:
        return palindromes
    generate_palindromes('', letters)
    return set((p for p in palindromes if p == p[::-1]))