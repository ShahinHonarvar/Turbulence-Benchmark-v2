def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]

    def generate_palindromes(current, remaining):
        if len(current) >= 5:
            yield ''.join(current)
        for i, char in enumerate(remaining):
            new_remaining = remaining[:i] + remaining[i + 1:]
            yield from generate_palindromes(current + [char] + current[::-1], new_remaining)
    return set(generate_palindromes([], letters))