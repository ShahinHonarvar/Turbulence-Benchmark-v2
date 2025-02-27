def return_nth_smallest_ascii(mystr):
    ascii_values = []
    for char in mystr[0:17]:
        ascii_values.append(ord(char))
    ascii_values.sort()
    return chr(ascii_values[16])