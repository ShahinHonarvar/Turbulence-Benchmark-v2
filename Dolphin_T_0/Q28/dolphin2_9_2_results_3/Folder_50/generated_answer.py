def return_nth_smallest_ascii(input_string):
    sub_string = input_string[25:89]
    sorted_chars = sorted(set(sub_string), key=ord)
    return sorted_chars[10] if len(sorted_chars) > 10 else None