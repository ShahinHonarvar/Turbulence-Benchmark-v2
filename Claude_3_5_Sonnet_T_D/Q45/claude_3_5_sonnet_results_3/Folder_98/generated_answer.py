def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[3:6] if c.isalpha()))
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4:
            result.add(current)
        if len(remaining) > 0:
            for char in remaining:
                new_remaining = remaining.copy()
                new_remaining.remove(char)
                generate_palindromes(char + current + char, new_remaining)
    generate_palindromes('', letters)
    return result