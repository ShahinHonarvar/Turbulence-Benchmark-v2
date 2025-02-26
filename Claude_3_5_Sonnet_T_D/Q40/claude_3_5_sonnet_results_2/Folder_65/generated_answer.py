def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort(key=lambda x: ord(x))
    result = char_list[:27] if len(char_list) >= 27 else char_list + [chr(i) for i in range(97, 97 + 27 - len(char_list))]
    return sorted(result, reverse=True)