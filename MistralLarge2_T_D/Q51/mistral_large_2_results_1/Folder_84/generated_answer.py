from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            count += len(anagram_dict[sorted_string])
        anagram_dict[sorted_string].append(string)
    return count <= 16