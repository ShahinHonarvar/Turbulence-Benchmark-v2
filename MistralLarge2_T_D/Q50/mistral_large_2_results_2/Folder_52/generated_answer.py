from collections import defaultdict

def if_contains_anagrams(strings):

    def normalized(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            norm = normalized(s)
            anagram_dict[norm].append(s)
    anagram_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values() if len(lst) > 1))
    return anagram_count >= 58