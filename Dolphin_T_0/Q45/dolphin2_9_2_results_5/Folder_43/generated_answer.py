from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[2:6]
    palindromes = set()
    for i in range(4, len(sub_string) + 1):
        perms = permutations(sub_string, i)
        for p in perms:
            string = ''.join(p)
            if string == string[::-1]:
                palindromes.add(string.lower())
    return palindromes