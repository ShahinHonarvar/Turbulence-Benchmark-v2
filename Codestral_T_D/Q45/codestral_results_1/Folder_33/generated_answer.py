import itertools

def palindromes_between_indices(s):
    s = s[7:10].lower()
    palindromes = set()
    for perm in itertools.permutations(s):
        for i in range(4, len(perm) + 1):
            sub_str = ''.join(perm[:i])
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes