from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = sorted_str(word)
            anagram_dict[key] += 1
    count = 0
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count >= 46:
                return True
    return False