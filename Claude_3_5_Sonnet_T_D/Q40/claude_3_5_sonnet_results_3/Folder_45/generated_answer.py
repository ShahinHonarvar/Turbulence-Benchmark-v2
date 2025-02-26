def return_n_smallest_chars(s):
    char_list = list(set(s))
    char_list.sort()
    return char_list[:52] if len(char_list) >= 52 else char_list + [chr(i) for i in range(128) if chr(i) not in char_list][:52 - len(char_list)]