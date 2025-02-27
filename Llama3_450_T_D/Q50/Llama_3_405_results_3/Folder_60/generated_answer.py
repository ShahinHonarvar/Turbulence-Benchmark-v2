from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        anagrams[sorted_str].append(s)
    count = 0
    for value in anagrams.values():
        value_len = len(value)
        if value_len > 1 and len(value[0]) >= 3:
            count += value_len * (value_len - 1) // 2
    return count >= 60