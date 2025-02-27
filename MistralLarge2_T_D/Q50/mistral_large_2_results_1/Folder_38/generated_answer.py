from collections import defaultdict

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    pairs = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    for group in anagram_dict.values():
        if len(group) > 1:
            pairs += len(group) * (len(group) - 1) // 2
    return pairs >= 24