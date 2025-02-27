import collections

def if_contains_anagrams(strList):
    anagram_dict = collections.defaultdict(list)
    for string in strList:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        anagram_dict[sorted_string].append(string)
    pairs = 0
    for anagram_list in anagram_dict.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs <= 78