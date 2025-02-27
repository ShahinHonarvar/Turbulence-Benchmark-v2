from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        anagram_dict[key].append(string)
    anagram_count = sum((1 for group in anagram_dict.values() if len(group) >= 2))
    return anagram_count >= 70