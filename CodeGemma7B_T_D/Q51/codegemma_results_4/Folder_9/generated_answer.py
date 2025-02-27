def if_contains_anagrams(str_list):
    str_dict = {}
    str_touched = set()
    pair_count = 0
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in str_dict and sorted_str not in str_touched:
            str_touched.add(sorted_str)
            str_touched.add(str_dict[sorted_str])
            pair_count += 1
        if sorted_str not in str_dict:
            str_dict[sorted_str] = string
        if pair_count > 475:
            return False
    return True