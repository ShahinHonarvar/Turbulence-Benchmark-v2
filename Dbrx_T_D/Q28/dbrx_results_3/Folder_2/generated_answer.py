def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(c) for c in input_string if 48 <= ord(c) <= 76]
    if len(ascii_list) >= 5:
        return chr(sorted(ascii_list)[5])
    else:
        return None