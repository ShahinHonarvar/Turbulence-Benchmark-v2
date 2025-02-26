def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[6:10] if c.isalpha()))

    def generate_palindromes(chars, min_length):
        result = set()
        n = len(chars)
        for i in range(n):
            for j in range(i, n):
                substring = chars[i:j + 1]
                if len(substring) >= min_length and substring == substring[::-1]:
                    result.add(substring)
        return result

    def permutations(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            for perm in permutations(chars[:i] + chars[i + 1:]):
                result.add(c + perm)
        return result
    all_perms = permutations(letters)
    palindromes = set()
    for perm in all_perms:
        palindromes.update(generate_palindromes(perm, 3))
    return palindromes