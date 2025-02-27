def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for p in generate_palindromes(letters[i:i + length]):
                palindromes.add(p)
    return palindromes

def generate_palindromes(letters):
    if len(letters) == 1:
        yield letters[0]
    elif len(letters) == 2:
        yield (letters[0] + letters[1])
        yield (letters[1] + letters[0])
    else:
        for i in range(len(letters)):
            for p in generate_palindromes(letters[:i] + letters[i + 1:]):
                yield (letters[i] + p + letters[i])