def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]

    def generate_palindromes(chars, current='', left=0, right=0):
        if len(current) >= 6:
            yield current
        if left + right < len(chars):
            for i, char in enumerate(chars):
                if i > 0 and char == chars[i - 1]:
                    continue
                if left <= right:
                    yield from generate_palindromes(chars[:i] + chars[i + 1:], char + current + char, left + 1, right + 1)
                else:
                    yield from generate_palindromes(chars[:i] + chars[i + 1:], current, left, right + 1)
    return set(generate_palindromes(letters))