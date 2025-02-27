def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string[15:22] if char >= input_string[15] and char <= input_string[21]]
    ascii_list.sort()
    return chr(ascii_list[5])