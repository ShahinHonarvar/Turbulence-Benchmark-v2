def return_nth_smallest_ascii(input_string):
    relevant_ascii_values = [ord(char) for char in input_string if 60 <= input_string.index(char) <= 83]
    relevant_ascii_values.sort()
    return chr(relevant_ascii_values[13])