from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_lowercase(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    anagrams_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = sorted_lowercase(word)
            anagram_pairs += anagrams_dict[key]
            anagrams_dict[key] += 1
            if anagram_pairs >= 46:
                return True
    return anagram_pairs >= 46