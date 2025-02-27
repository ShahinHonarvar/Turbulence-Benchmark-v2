from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        anagrams[sorted_string].append(string)
    anagram_count = sum((len(v) for v in anagrams.values() if len(v) > 1))
    return anagram_count <= 49