from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        anagram_dict[key].append(string)
    anagram_pairs = sum((len(group) // 2 for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs >= 14