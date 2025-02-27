from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(4):
        letters[s[i].lower()] += 1
    palindromes = set()
    for combination in itertools.product(letters, repeat=4):
        string = ''.join(itertools.islice(filter(lambda x: x is not None, (k if v > 0 else None for k, v in combination)), 4))
        if len(string) == 4 and string == string[::-1]:
            palindromes.add(string.upper())
    return palindromes