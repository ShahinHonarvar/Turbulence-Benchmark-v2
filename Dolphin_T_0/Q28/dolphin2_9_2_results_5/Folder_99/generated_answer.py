def return_nth_smallest_ascii(string):
    if not 17 <= 65 <= len(string):
        return 'Indices out of bounds'
    ascii_list = []
    for i in range(17, 66):
        ascii_list.append(ord(string[i]))
    ascii_list.sort()
    return chr(ascii_list[7])