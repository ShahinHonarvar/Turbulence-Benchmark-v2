from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    length_filtered = [s for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for s in length_filtered:
        sorted_s = ''.join(sorted(s.lower()))
        anagram_dict[sorted_s].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_pairs >= 81