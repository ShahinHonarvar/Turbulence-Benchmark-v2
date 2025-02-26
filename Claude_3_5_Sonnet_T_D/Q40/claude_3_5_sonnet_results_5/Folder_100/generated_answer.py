def return_n_smallest_chars(s):
    char_list = list(set(s))
    char_list.sort(key=lambda x: ord(x))
    result = char_list[:72]
    result.sort(reverse=True)
    return result