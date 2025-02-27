def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string[4:34] if char != ' ']
    ascii_list.sort()
    if len(ascii_list) >= 4:
        return chr(ascii_list[3])
    else:
        return None