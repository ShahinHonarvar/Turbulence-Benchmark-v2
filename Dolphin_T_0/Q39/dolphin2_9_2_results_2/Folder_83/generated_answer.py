def return_n_greatest_chars(s):
    s_list = [ord(char) for char in sorted(s)]
    s_list.sort(reverse=True)
    s_list = s_list[:38]
    return s_list