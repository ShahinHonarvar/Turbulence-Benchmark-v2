def return_n_greatest_chars(s):
    char_list = list(set(s))
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return sorted(char_list[:52])