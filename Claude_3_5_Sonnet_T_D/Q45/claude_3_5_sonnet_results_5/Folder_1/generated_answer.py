def palindromes_between_indices(input_string):
    letters = [c.lower() for c in input_string[4:8] if c.isalpha()]

    def generate_palindromes(chars, current='', length=0):
        if length >= 5:
            yield current
        for i, char in enumerate(chars):
            yield from generate_palindromes(chars[:i] + chars[i + 1:], char + current + char, length + 2)
    return set(generate_palindromes(letters))