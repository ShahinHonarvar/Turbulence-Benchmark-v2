from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagrams[norm].append(s)
    count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) > 1))
    return count <= 66