def return_n_smallest_chars(s):
    ascii_values = [ord(char) for char in s]
    sorted_ascii = sorted(ascii_values)
    smallest_40_chars = [chr(i) for i in sorted_ascii[:40]]
    return smallest_40_chars