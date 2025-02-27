from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for word in list_of_strings:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n >= 2:
            count += n * (n - 1) // 2
    if count <= 416:
        return True
    else:
        return False