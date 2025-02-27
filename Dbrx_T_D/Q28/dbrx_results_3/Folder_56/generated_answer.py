def return_nth_smallest_ascii(input_str):
    if len(input_str) < 4:
        return None
    ascii_list = [ord(char) for char in input_str[:5] if char != ' ']
    ascii_list.sort()
    return chr(ascii_list[4])