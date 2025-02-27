from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str] += 1
    count_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return count_pairs >= 16