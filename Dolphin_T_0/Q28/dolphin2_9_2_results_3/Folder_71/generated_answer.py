def return_nth_smallest_ascii(s):
    substring = s[5:83]
    ascii_list = [ord(ch) for ch in substring]
    ascii_list.sort()
    return chr(ascii_list[15])