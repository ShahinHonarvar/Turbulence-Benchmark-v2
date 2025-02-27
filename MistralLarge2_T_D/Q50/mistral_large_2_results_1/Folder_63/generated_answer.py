from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagram_dict[key] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs_count >= 89