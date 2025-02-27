from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower().replace(' ', '')))
            if key in anagram_counts:
                anagram_counts[key] += 1
            else:
                anagram_counts[key] = 1
    return sum((count // 2 for count in anagram_counts.values())) <= 8