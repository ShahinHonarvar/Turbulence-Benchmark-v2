from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for word in list_of_strings:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for key, value in anagram_dict.items():
        if len(value) >= 2:
            count += len(value) * (len(value) - 1) // 2
    if count <= 26:
        return True
    else:
        return False