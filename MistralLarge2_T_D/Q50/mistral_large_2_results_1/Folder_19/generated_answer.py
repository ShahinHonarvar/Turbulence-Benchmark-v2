from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_count[sorted_str].append(string)
    pair_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_count.values() if len(group) > 1))
    return pair_count >= 84