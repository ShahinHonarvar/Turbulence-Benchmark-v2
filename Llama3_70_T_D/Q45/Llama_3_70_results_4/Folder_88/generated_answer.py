from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = s[3:8]
    sub_string = ''.join(filter(str.isalpha, sub_string))
    if len(sub_string) < 3:
        return set()
    palindromes = set()
    for p in range(6, len(sub_string) + 1):
        for perm in permutations(sub_string, p):
            perm = ''.join(perm)
            rev = perm[::-1]
            if perm == rev:
                palindromes.add(perm)
    return palindromes