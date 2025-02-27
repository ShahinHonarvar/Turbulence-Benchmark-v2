from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for string in list_of_strings:
        if len(string) < 3:
            continue
        anagram_dict[''.join(sorted(string.lower()))].append(string)
    count = 0
    for key, value in anagram_dict.items():
        if len(value) >= 2:
            count += 1
    if count <= 2:
        return True
    else:
        return False