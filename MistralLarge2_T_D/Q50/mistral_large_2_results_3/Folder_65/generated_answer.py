from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_count[sorted_str] += 1
    pairs_count = 0
    for count in anagram_count.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count >= 94