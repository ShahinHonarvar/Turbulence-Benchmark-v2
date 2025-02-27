def palindromes_between_indices(text):
    letters = text[1:6].lower()
    palindromes = set()
    for p in permutation_finder(letters):
        if len(p) >= 4 and p == p[::-1]:
            palindromes.add(p)
    return palindromes

def permutation_finder(string):
    if len(string) == 1:
        yield string
    else:
        for i, char in enumerate(string):
            remaining = string[:i] + string[i + 1:]
            for perm in permutation_finder(remaining):
                yield (char + perm)