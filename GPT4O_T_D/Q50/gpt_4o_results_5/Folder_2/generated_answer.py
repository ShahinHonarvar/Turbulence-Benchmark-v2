from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagrams_dict = defaultdict(int)
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_str(s)
            anagrams_dict[sorted_s] += 1
    for value in anagrams_dict.values():
        if value >= 2:
            count += value * (value - 1) // 2
        if count >= 246:
            return True
    return False