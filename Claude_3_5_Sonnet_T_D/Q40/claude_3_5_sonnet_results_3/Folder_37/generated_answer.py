def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort(key=lambda x: ord(x))
    result = char_list[:26] if len(char_list) >= 26 else char_list + [chr(i) for i in range(ord('a'), ord('z') + 1)]
    result = result[:26]
    result.sort(reverse=True)
    return result