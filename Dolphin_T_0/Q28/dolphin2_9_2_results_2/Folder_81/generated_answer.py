def return_nth_smallest_ascii(s):
    ascii_values = list()
    for i in range(14):
        ascii_values.append(ord(s[i]))
    ascii_values.sort()
    return chr(ascii_values[13])