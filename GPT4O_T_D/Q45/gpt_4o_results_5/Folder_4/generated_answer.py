from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = ''.join(filter(str.isalpha, s[3:10]))
    if len(sub_string) < 7:
        return set()
    palindromes = set()
    for p in permutations(sub_string, 7):
        if p[:3] == p[-1:-4:-1]:
            palindromes.add(''.join(p))
    return palindromes