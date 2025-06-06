from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    count = 0
    for key in anagram_groups:
        if len(anagram_groups[key]) >= 2:
            count += 1
    if count <= 8:
        return True
    else:
        return False