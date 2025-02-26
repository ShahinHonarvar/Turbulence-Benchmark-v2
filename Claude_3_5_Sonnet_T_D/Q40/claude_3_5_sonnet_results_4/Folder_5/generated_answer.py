def return_n_smallest_chars(string):
    char_list = list(set(string))
    char_list.sort(key=lambda x: ord(x))
    result = char_list[:46]
    result.sort(reverse=True)
    return result