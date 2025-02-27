def all_substring_of_size_n(my_str):
    if len(my_str) < 2:
        return []
    n = 2
    sub_strings = [my_str[i:i + n] for i in range(len(my_str) - n + 1)]
    distinct_substrings = list(set(sub_strings))
    final_list = [s for s in distinct_substrings if len(set(s)) == n]
    return final_list