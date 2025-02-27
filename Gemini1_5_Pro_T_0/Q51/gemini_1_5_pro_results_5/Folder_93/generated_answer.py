from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for word in list_of_strings:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) / 2
    if count <= 36:
        return True
    else:
        return False