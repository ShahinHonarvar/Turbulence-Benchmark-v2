from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):

    def is_anagram(s):
        return all((v == 2 for v in Counter(s).values()))
    pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i].lower() + lst[j].lower()):
                    pairs.add((lst[i], lst[j]))
    return len(pairs) <= 366