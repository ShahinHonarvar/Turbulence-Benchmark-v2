def return_n_greatest_chars(s):
    char_list = list(s)
    char_list.sort(reverse=True)
    return sorted(char_list[0:43], reverse=True)