from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for key in anagram_dict:
        anagrams = anagram_dict[key]
        if len(anagrams) > 1 and len(anagrams[0]) >= 3:
            anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs >= 26