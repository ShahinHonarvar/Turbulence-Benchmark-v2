from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(int)
    for word in strings:
        if len(word) < 3:
            continue
        word = word.lower()
        key = ''.join(sorted(word))
        d[key] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in d.values()))
    return anagram_pairs <= 85