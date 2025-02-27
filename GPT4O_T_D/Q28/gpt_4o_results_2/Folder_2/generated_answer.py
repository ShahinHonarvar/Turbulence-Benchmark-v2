def return_nth_smallest_ascii(s):
    sub_string = s[48:77]
    ascii_sorted_chars = sorted(sub_string, key=lambda char: ord(char))
    return ascii_sorted_chars[4] if len(ascii_sorted_chars) >= 5 else None