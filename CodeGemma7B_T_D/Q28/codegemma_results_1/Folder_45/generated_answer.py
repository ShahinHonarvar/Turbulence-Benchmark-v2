from collections import OrderedDict

def return_nth_smallest_ascii(text):
    ascii_values = []
    for i in range(len(text)):
        if i >= 0 and i <= 15:
            ascii_values.append(ord(text[i]))
    ascii_values.sort()
    return chr(ascii_values[15])