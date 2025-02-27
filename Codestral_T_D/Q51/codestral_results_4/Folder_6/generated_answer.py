from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = Counter((''.join(sorted(s.lower())) for s in strings if len(s) >= 3))
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) <= 86