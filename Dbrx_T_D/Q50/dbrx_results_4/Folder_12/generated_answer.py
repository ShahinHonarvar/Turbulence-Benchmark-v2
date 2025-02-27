from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams_count = 0
    string_dict = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            string_dict[sorted_string].append(string)
    for strings in string_dict.values():
        if len(strings) >= 2:
            anagrams_count += len(strings) * (len(strings) - 1)
    return anagrams_count >= 69