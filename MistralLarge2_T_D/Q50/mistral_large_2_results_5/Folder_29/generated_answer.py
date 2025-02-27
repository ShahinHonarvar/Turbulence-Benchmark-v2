from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    anagram_count = sum((1 for anagrams in anagram_dict.values() if len(anagrams) >= 2))
    return anagram_count >= 35