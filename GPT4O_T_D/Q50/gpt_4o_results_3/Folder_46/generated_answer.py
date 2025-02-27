from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = sorted_str(word)
            anagram_dict[key].append(word)
    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
            if anagram_pairs >= 38:
                return True
    return False