from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = Counter()
    for word in lst:
        if len(word) >= 3:
            anagram_count[''.join(sorted(word.lower()))] += 1
    return sum((v * (v - 1) // 2 for v in anagram_count.values())) >= 16