from collections import Counter

def if_contains_anagrams(lst):
    anagrams = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    anagram_count = Counter(anagrams)
    return sum((n * (n - 1) // 2 for n in anagram_count.values())) <= 206