def return_nth_smallest_ascii(my_string):
    ascii_values = [ord(char) for char in my_string[29:48] if my_string.index(char) >= 29 and my_string.index(char) <= 47]
    ascii_values.sort()
    return ascii_values[6]