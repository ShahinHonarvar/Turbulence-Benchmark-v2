from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_count[sorted_string] += 1
    pair_count = 0
    for count in anagram_count.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
    return pair_count >= 46