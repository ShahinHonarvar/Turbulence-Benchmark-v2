def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort(key=ord)
    result = char_list[:66] if len(char_list) >= 66 else char_list + [chr(0)] * (66 - len(char_list))
    return sorted(result, reverse=True)