def palindromes_between_indices(s):
    s = s[6:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for p in generate_palindromes(letters[i:i + length]):
                palindromes.add(''.join(p))
    return palindromes

def generate_palindromes(letters):
    if len(letters) == 1:
        yield letters
    elif len(letters) == 2:
        yield letters
        yield list(reversed(letters))
    else:
        for i in range(len(letters)):
            for p in generate_palindromes(letters[:i] + letters[i + 1:]):
                yield ([letters[i]] + p + [letters[i]])