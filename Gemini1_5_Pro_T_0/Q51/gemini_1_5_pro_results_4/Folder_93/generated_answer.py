from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagram_dict[''.join(sorted(string.lower()))].append(string.lower())
    count = 0
    for key, value in anagram_dict.items():
        count += len(value) * (len(value) - 1) // 2
    if count <= 36:
        return True
    else:
        return False