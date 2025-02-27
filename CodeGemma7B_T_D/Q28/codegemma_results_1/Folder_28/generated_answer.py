def return_nth_smallest_ascii(char_str):
    ascii_list = sorted([ord(c) for c in char_str if ord(c) >= ord('a') and ord(c) <= ord('z') and (25 <= char_str.index(c) <= 77)])
    return chr(ascii_list[15])