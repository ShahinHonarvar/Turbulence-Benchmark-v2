from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(lambda: [])
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    count = 0
    for sorted_string in anagram_dict:
        n = len(anagram_dict[sorted_string])
        count += n * (n - 1) // 2
    if count > 407:
        return False
    else:
        return True