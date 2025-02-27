from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    anagram_pairs = 0
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        count[key] += 1
        if count[key] == 2:
            anagram_pairs += 1
        elif count[key] > 2:
            anagram_pairs += count[key] - 1
    return anagram_pairs >= 276