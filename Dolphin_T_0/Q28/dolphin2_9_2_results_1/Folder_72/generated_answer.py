def return_nth_smallest_ascii(my_string):
    char_values = [ord(char) for char in my_string if 33 <= my_string.index(char) <= 60]
    sorted_char_values = sorted(list(set(char_values)))
    return chr(sorted_char_values[17])