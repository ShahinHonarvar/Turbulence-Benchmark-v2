from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) - 1
        if count > 279:
            return False
    return True