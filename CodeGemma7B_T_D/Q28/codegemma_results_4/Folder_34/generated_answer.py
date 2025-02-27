def return_nth_smallest_ascii(char_string):
    ascii_values = {c: ord(c) for c in char_string[:19]}
    return min(ascii_values, key=ascii_values.get)