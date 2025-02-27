from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        key = sort_chars(s)
        anagrams[key] += 1
    count_pairs = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return count_pairs <= 147