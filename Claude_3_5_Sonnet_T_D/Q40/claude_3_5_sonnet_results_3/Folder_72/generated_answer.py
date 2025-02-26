def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort(key=lambda x: ord(x))
    result = char_list[:37]
    result.sort(reverse=True)
    return result