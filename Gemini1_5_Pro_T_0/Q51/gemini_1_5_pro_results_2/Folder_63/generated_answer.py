from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagram_dict[''.join(sorted(string.lower()))].append(string.lower())
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        count += n * (n - 1) // 2
    if count <= 423:
        return True
    else:
        return False