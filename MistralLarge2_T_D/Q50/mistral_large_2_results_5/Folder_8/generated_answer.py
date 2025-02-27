from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_count[sorted_string].append(string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_count.values() if len(group) > 1))
    return anagram_pairs >= 85