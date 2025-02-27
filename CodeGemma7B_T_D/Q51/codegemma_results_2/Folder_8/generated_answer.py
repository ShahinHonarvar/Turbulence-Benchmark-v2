def if_contains_anagrams(str_list):
    str_counts = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in str_counts:
            str_counts[sorted_string] = 1
        else:
            str_counts[sorted_string] += 1
        if str_counts[sorted_string] > 68:
            return False
    return True