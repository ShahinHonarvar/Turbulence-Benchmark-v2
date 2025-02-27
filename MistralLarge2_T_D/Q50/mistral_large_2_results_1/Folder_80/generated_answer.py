from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagram_count[key] += 1
    anagram_pairs = sum((count // 2 for count in anagram_count.values()))
    return anagram_pairs >= 19