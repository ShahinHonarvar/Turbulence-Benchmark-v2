from collections import Counter

def if_contains_anagrams(strings):
    cnt = Counter()
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        cnt[key] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in cnt.values()))
    return anagram_pairs <= 401