from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            norm_word = normalize(word)
            anagram_dict[norm_word].append(word)
    anagram_pairs = sum((1 for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs >= 8