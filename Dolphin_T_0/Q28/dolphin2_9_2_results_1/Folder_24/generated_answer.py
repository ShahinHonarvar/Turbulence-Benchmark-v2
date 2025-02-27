def return_nth_smallest_ascii(s):
    ascii_list = [ord(ch) for ch in s[34:82]]
    ascii_list.sort()
    return chr(ascii_list[11])