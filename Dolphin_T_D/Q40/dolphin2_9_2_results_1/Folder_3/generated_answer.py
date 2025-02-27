def return_n_smallest_chars(input_str):
    if len(input_str) < 28:
        return 'Input string is not long enough.'
    elif len(set(input_str)) != len(input_str):
        return 'Input string has duplicated characters.'
    char_list = list(input_str)
    char_list.sort()
    smallest_chars = char_list[:28]
    smallest_chars.sort(reverse=True)
    return smallest_chars