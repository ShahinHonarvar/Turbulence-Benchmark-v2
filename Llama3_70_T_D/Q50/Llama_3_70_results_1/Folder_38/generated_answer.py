from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams_count[sorted_string] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs_count >= 24