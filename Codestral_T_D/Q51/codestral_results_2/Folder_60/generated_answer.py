from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            anagrams.append(''.join(sorted(word.lower())))
    anagram_count = Counter(anagrams)
    pair_count = sum([count * (count - 1) // 2 for count in anagram_count.values()])
    return pair_count <= 77