from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    count = 0
    for key, value in anagram_dict.items():
        count += len(value) * (len(value) - 1) // 2
    if count > 61:
        return False
    else:
        return True