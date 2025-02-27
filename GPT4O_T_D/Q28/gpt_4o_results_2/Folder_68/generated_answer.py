def return_nth_smallest_ascii(input_string):
    sub_string = input_string[:11]
    sorted_chars = sorted(sub_string)
    return sorted_chars[10] if len(sorted_chars) >= 11 else None