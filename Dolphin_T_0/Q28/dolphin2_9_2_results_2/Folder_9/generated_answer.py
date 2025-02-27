def return_nth_smallest_ascii(input_string):
    input_string = input_string[10:91]
    sorted_chars = sorted(input_string, key=lambda x: ord(x))
    return sorted_chars[19]