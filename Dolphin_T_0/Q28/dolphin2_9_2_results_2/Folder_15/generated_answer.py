def return_nth_smallest_ascii(s):
    ascii_list = [ord(c) for c in s[0:6]]
    ascii_list.sort()
    if len(ascii_list) >= 6:
        return chr(ascii_list[5])
    else:
        return None