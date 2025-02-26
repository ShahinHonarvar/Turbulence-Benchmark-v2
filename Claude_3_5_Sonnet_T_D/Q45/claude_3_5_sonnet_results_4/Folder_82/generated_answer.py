def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]

    def generate_palindromes(chars, current='', left=0, right=0):
        if len(current) >= 7:
            yield current
        if left < len(chars):
            yield from generate_palindromes(chars, chars[left] + current + chars[left], left + 1, right)
        if right < len(chars):
            yield from generate_palindromes(chars, current + chars[right], left, right + 1)
    return set(generate_palindromes(letters))