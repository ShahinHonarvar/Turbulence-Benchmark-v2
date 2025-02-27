def return_nth_smallest_ascii(s):
    ascii_list = [ord(ch) for ch in s[9:60] if 9 <= s.index(ch) <= 59]
    ascii_list.sort()
    return chr(ascii_list[5])