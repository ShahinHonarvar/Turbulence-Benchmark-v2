import itertools
    from collections import Counter

def palindromes_between_indices(s):
    palm = set()
    sub = s[2:10].lower()
    c = Counter(sub)

    def get_valid_pals(sub, length):
        subs = [i for i in list(itertools.permutations(sub, length)) if i == i[::-1]]
        subs.sort()
        seen = set()
        return [sub for sub in subs if sub not in seen and (not seen.add(sub))]
    lengths = [i for i in range(7, len(sub) + 1)]
    for length in lengths:
        palm.update(get_valid_pals(sub, length))
    if palm:
        return palm
    else:
        return set()