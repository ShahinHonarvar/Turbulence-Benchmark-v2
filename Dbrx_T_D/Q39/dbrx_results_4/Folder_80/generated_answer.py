def return_n_greatest_chars(string_of_chars):
    char_list = list(string_of_chars)
    char_list = sorted(char_list, key=ord)
    result = []
    for char in char_list[-35:]:
        result.append(char)
    return result[::-1]