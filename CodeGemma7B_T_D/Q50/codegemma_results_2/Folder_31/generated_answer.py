def if_contains_anagrams(list_of_strings):
    str_map = {}
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in str_map:
            str_map[sorted_string] = []
        str_map[sorted_string].append(string)
    count = 0
    for anagram_list in str_map.values():
        if len(anagram_list) >= 68:
            count += 1
    return count >= 68