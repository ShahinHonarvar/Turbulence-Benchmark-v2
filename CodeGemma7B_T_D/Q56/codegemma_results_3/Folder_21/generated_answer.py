from itertools import permutations

def all_substring_of_size_n(s):
    str_set = set()
    for i in range(len(s) - 106 + 1):
        for j in range(i, i + 106):
            str_set.add((''.join(p) for p in permutations(s[i:j + 1], 106)))
    return list(str_set)