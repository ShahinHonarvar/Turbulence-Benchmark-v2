import collections

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_dict = collections.defaultdict(list)
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams_dict[sorted_string].append(string)
    for string_list in anagrams_dict.values():
        if len(string_list) >= 2:
            anagrams_count += len(string_list) * (len(string_list) - 1) // 2
    return anagrams_count >= 209