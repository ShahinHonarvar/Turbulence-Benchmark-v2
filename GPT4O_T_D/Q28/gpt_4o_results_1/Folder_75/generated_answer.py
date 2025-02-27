def return_nth_smallest_ascii(input_string):
    sub_string = input_string[62:84]
    sorted_chars = sorted(sub_string)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None