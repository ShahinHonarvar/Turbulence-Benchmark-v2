from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            anagram_dict[sorted_str].append(s)
    anagram_pairs_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values() if len(anagrams) > 1))
    return anagram_pairs_count >= 59