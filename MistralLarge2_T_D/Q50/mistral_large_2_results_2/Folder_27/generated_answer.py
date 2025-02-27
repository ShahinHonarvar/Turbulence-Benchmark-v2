from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        anagram_count[key].append(string)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_count.values() if len(v) > 1))
    return pairs >= 86