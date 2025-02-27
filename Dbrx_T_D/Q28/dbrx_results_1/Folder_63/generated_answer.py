def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string if 47 <= ord(char) <= 70]
    ascii_list.sort()
    return chr(ascii_list[13])