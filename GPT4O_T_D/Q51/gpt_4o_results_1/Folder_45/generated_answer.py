from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_groups[sorted_string(word)].append(word)
    anagram_pairs = 0
    for anagram_list in anagram_groups.values():
        n = len(anagram_list)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 464