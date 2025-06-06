def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[4:6] if c.isalpha()))
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                result.add(current)
        for char in remaining:
            new_remaining = remaining.copy()
            new_remaining.remove(char)
            generate_palindromes(current + char, new_remaining)
            generate_palindromes(char + current, new_remaining)
    generate_palindromes('', letters)
    return result