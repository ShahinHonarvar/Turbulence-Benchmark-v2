def if_contains_anagrams(str_list):
    str_map = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in str_map:
            str_map[sorted_string] = [string]
        else:
            str_map[sorted_string].append(string)
    count = 0
    for anagrams in str_map.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 136