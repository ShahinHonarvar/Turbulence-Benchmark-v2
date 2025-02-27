def return_nth_smallest_ascii(string):
    characters = string[1:37]
    ascii_values = [ord(char) for char in characters]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[14])