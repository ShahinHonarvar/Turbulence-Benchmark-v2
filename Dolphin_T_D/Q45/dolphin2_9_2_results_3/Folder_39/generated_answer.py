from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(string):
    string = string[2:6].lower()
    palindromes = set()
    for i in range(3, len(string) + 1):
        for p in permutations(string, i):
            if ''.join(p) == ''.join(p[::-1]) and set(p) <= set(ascii_lowercase):
                palindromes.add(''.join(p))
    return palindromes