from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_dict[normalized].append(s)
    count = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            pairs = len(anagram_list) * (len(anagram_list) - 1) // 2
            count += pairs
            if count > 70:
                return False
    return True