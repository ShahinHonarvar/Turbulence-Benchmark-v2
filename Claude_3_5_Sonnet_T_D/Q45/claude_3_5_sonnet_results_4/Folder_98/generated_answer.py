def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[3:6] if c.isalpha()))

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and current == current[::-1]:
            palindromes.add(current)
        if len(current) < 8:
            for char in remaining:
                new_remaining = remaining.copy()
                new_remaining.remove(char)
                generate_palindromes(char + current + char, new_remaining)
    palindromes = set()
    generate_palindromes('', letters)
    return palindromes