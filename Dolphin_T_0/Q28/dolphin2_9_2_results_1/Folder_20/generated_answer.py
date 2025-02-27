def return_nth_smallest_ascii(s):
    ascii_list = []
    for i in range(25, 65):
        ascii_list.append(ord(s[i]))
    ascii_list.sort()
    return chr(ascii_list[5])