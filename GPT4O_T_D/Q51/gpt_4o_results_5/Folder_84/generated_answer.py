from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_str(s)
            anagram_dict[sorted_s] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagrams_count += count * (count - 1) // 2
            if anagrams_count > 16:
                return False
    return True