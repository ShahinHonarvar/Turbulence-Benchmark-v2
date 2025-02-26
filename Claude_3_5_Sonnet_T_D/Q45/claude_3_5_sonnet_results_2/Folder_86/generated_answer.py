def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[6:10] if c.isalpha()))

    def generate_palindromes(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            rest = chars[:i] + chars[i + 1:]
            for p in generate_palindromes(rest):
                result.add(c + p + c)
        return result
    all_palindromes = generate_palindromes(letters)
    return set((p for p in all_palindromes if len(p) >= 4))