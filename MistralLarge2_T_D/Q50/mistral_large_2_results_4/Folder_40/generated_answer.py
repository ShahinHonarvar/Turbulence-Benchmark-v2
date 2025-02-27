from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counter = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_counter[sorted_string] += 1
    pairs_count = sum((count // 2 for count in anagram_counter.values() if count >= 2))
    return pairs_count >= 3