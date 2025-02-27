def if_contains_anagrams(str_list):
    str_count = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str not in str_count:
            str_count[sorted_str] = 0
        str_count[sorted_str] += 1
    if sum(str_count.values()) <= 68:
        return True
    return False