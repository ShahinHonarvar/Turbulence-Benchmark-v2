def return_nth_smallest_ascii(s):
    ascii_values = {ord(char): char for char in s[25:89]}
    sorted_ascii_values = sorted(ascii_values.keys())
    return ascii_values[sorted_ascii_values[10]]