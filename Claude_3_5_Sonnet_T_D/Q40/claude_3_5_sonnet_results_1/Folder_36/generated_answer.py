def return_n_smallest_chars(s):
    char_list = sorted(set(s))
    return char_list[:32] if len(char_list) >= 32 else char_list + [chr(i) for i in range(128) if chr(i) not in char_list][:32 - len(char_list)]