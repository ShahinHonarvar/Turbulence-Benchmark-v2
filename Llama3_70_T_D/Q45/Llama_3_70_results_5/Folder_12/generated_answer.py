import itertools

def palindromes_between_indices(s):
    sub_string = s[3:9].lower()
    sub_string = ''.join(filter(str.isalpha, sub_string))
    palindromes = set()
    for r in range(4, len(sub_string) + 1):
        for combo in itertools.combinations(sub_string, r):
            for perm in itertools.permutations(combo):
                if perm == perm[::-1]:
                    palindromes.add(''.join(perm))
    return palindromes