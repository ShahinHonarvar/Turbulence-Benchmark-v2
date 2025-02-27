def if_contains_anagrams(str_list):
    str_set = set()
    count = 0
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in str_set:
            str_set.add(sorted_string)
            count += 1
    return count >= 65