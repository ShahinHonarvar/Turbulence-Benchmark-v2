def return_nth_smallest_ascii(s):
    ascii_table = [ord(ch) for ch in s[1:47]]
    ascii_table.sort()
    return chr(ascii_table[12])