def return_n_smallest_chars(s):
    char_list = sorted(set(s))
    return char_list[:37] if len(char_list) >= 37 else char_list + [chr(i) for i in range(128) if chr(i) not in char_list][:37 - len(char_list)]