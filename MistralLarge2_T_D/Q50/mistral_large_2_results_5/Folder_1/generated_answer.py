from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    anagram_pairs = sum((len(group) // 2 for group in anagram_dict.values() if len(group) >= 2))
    return anagram_pairs >= 96