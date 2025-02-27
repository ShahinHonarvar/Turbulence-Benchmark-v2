def return_nth_smallest_ascii(input_string):
    chars_between_indices_0_to_9 = input_string[0:10]
    ascii_values_of_chars = sorted((ord(char) for char in chars_between_indices_0_to_9 if char in chars_between_indices_0_to_9))
    return chr(ascii_values_of_chars[9])