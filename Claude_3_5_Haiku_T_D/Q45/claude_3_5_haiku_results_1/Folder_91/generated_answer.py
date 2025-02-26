def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(current) == 2 * (len(current) // 2) + 1:
            palindromes.add(current)
        for i in range(len(remaining)):
            letter = remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(current + letter, new_remaining)
            if len(current) > 0:
                generate_palindromes(letter + current, new_remaining)
    generate_palindromes('', letters)
    return {p for p in palindromes if p == p[::-1] and len(p) >= 3}