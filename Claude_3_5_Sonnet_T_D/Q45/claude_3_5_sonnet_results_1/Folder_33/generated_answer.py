def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[7:10] if c.isalpha()))

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            rest = chars[:i] + chars[i + 1:]
            for p in generate_palindromes(rest, length - 2):
                result.add(c + p + c)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes