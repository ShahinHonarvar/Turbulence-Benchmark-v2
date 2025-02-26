def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:7] if c.isalpha()))

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            remaining = chars[:i] + chars[i + 1:]
            sub_palindromes = generate_palindromes(remaining, length - 2)
            for sub in sub_palindromes:
                result.add(c + sub + c)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes