def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:10] if c.isalpha()))

    def generate_palindromes(chars, current='', results=None):
        if results is None:
            results = set()
        if len(current) >= 7 and current == current[::-1]:
            results.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char, results)
        return results
    return generate_palindromes(letters)