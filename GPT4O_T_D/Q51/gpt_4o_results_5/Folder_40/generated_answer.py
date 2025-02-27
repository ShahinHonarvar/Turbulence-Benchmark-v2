from collections import defaultdict

def if_contains_anagrams(lst):

    def char_count(s):
        return tuple(sorted([c.lower() for c in s if c.isalpha()]))
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_key = char_count(word)
            anagram_dict[anagram_key] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 29:
                return False
    return True