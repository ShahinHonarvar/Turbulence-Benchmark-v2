from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    ana_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            ana_dict[sorted_str(s)] += 1
    pairs = 0
    for count in ana_dict.values():
        pairs += count * (count - 1) // 2
        if pairs >= 86:
            return True
    return False