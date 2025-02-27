def return_nth_smallest_ascii(s):
    subset_s = s[25:78]
    ascii_list = [ord(x) for x in subset_s]
    ascii_list.sort()
    return chr(ascii_list[15])