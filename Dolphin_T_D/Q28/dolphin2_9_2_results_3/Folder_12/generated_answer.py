def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(3, 27):
        ascii_values.append(ord(s[i]))
    ascii_values.sort()
    return chr(ascii_values[4])