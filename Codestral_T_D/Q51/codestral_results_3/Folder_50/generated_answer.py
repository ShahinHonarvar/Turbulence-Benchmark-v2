from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            cnt[key] += 1
    num_anagram_pairs = sum((value * (value - 1) // 2 for value in cnt.values()))
    return num_anagram_pairs <= 47