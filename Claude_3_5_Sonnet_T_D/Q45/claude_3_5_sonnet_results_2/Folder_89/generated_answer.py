def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]

    def generate_palindromes(chars, current='', length=0):
        if length >= 6:
            yield current
        if chars:
            for i, char in enumerate(chars):
                yield from generate_palindromes(chars[:i] + chars[i + 1:], char + current + char, length + 2)
    return set(generate_palindromes(letters))