def return_nth_smallest_ascii(s):
    sub_str = s[8:27]
    ascii_val_list = [ord(c) for c in sub_str if c in sub_str]
    ascii_val_list.sort()
    return chr(ascii_val_list[5])