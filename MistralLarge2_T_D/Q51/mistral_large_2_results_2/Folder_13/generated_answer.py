from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_count[sorted_str].append(s)
    anagram_pairs = 0
    for key in anagram_count:
        if len(anagram_count[key]) > 1:
            pairs = len(anagram_count[key]) * (len(anagram_count[key]) - 1) // 2
            anagram_pairs += pairs
    return anagram_pairs <= 54