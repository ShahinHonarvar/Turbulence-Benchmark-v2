from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += 1
    if count <= 8:
        return True
    else:
        return False