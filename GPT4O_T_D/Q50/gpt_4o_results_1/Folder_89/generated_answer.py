from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[sorted_str(s)] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 36:
                return True
    return False