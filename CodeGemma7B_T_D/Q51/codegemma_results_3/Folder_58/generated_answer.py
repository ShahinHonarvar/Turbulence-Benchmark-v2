import collections

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    anagram_dict = collections.defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    num_pairs = 0
    for anagram_group in anagram_dict.values():
        num_pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return num_pairs <= 60