def return_nth_smallest_ascii(s):
    ascii_values = {}
    for i in range(5, 90):
        ascii_values[s[i]] = ord(s[i])
    sorted_ascii = sorted(ascii_values.items(), key=lambda x: x[1])
    return sorted_ascii[12][0]