from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_dict[sorted_str].append(string)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) - 1
    return count <= 50