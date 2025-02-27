def palindromes_between_indices(s: str) -> set:
    valid_chars = [c.lower() for c in s[5:10] if c.isalpha()]
    palindromes = {word for word in {''.join(p) for p in itertools.product(valid_chars, repeat=6)} if word == word[::-1]}
    return palindromes