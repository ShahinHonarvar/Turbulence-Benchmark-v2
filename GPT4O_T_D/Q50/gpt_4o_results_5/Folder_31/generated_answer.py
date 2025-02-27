from collections import defaultdict

def if_contains_anagrams(strings):
    ana_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            ana_dict[sorted_str] += 1
    pair_count = 0
    for count in ana_dict.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
    return pair_count >= 68