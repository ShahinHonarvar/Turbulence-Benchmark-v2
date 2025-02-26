def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]

    def generate_palindromes(chars, current='', length=0):
        if length >= 6:
            yield current
        for i, char in enumerate(chars):
            new_chars = chars[:i] + chars[i + 1:]
            yield from generate_palindromes(new_chars, char + current + char, length + 2)
    return set(generate_palindromes(letters))