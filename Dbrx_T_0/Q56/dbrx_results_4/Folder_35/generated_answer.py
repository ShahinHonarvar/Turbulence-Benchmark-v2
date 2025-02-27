from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 26):
        for perm in permutations(s[i:i + 27]):
            t = ''.join(perm)
            if len(t) == 27 and len(set(t)) == 27:
                result.add(t)
    return list(result)