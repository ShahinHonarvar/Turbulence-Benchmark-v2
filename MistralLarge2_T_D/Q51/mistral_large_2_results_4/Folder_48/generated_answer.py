from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_count[sorted_string].append(string)
    pairs = 0
    for key, group in anagram_count.items():
        n = len(group)
        pairs += n * (n - 1) // 2
    return pairs <= 277