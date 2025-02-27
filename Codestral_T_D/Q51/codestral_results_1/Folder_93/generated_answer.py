from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = Counter((''.join(sorted(word.lower())) for word in lst if len(word) >= 3))
    return sum((count * (count - 1) // 2 for count in anagram_counter.values())) <= 36