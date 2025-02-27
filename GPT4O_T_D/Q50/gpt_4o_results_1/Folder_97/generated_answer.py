from collections import defaultdict

def if_contains_anagrams(strings):

    def is_valid_anagram_pair(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    sorted_str_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            sorted_str_dict[sorted_str] += 1
    count = 0
    for val in sorted_str_dict.values():
        count += val * (val - 1) // 2
        if count >= 123:
            return True
    return False