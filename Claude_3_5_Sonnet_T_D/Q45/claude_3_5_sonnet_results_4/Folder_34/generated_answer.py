def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[5:8] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current='', length=0):
        if length >= 4 and is_palindrome(current):
            yield current
        if length < 8:
            for char in chars:
                yield from generate_palindromes(chars, char + current + char, length + 2)
    return set(generate_palindromes(letters))