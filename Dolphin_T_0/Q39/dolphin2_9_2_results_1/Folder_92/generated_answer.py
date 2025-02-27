def return_n_greatest_chars(input_string):
    n = 63
    char_list = list(input_string)
    char_list.sort(key=lambda c: -ord(c))
    return [char_list[i] for i in range(n)]