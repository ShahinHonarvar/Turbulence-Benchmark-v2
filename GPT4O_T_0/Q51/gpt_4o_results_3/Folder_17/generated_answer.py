from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_dict[sorted_s] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 22:
                return False
    return True