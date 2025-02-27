from collections import defaultdict

def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_count[sorted_str] += 1
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_of_anagrams >= 64