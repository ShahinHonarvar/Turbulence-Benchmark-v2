def palindromes_between_indices(s):
    s = s.lower()
    letters = set(s[1:5])
    letters = {c for c in letters if c.isalpha()}
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for p in generate_palindromes(letters, length):
            palindromes.add(p)
    return palindromes

def generate_palindromes(letters, length):
    if length == 1:
        for letter in letters:
            yield letter
    elif length == 2:
        for letter in letters:
            yield (letter * 2)
    else:
        for letter in letters:
            for p in generate_palindromes(letters - {letter}, length - 2):
                yield (letter + p + letter)