def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:7] if c.isalpha()))

    def generate_palindromes(chars, current='', left='', right=''):
        if len(current) >= 6:
            yield (left + current + right)
        if len(chars) > 0:
            for i, c in enumerate(chars):
                new_chars = chars[:i] + chars[i + 1:]
                yield from generate_palindromes(new_chars, current + c, left, right)
                yield from generate_palindromes(new_chars, current, left + c, c + right)
    return set((p for p in generate_palindromes(letters) if len(p) >= 6))