def return_nth_smallest_ascii(input_string):
    sub_string = input_string[28:55]
    sorted_chars = sorted(set(sub_string), key=lambda x: ord(x))
    return sorted_chars[13]