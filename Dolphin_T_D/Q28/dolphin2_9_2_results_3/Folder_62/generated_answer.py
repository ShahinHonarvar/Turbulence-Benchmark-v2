def return_nth_smallest_ascii(string):
    ascii_values_in_range = [string[i] for i in range(51, 79) if string[i].isalpha()]
    sorted_values = sorted(ascii_values_in_range, key=lambda x: ord(x))
    return sorted_values[9 - 1]