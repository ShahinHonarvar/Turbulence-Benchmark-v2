from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = sorted_string(word)
            anagram_dict[sorted_word].append(word)
    anagram_pairs_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs_count >= 43