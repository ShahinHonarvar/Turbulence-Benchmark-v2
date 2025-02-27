def return_nth_smallest_ascii(input_string):
    substring = input_string[13:35]
    sorted_chars = sorted(list(substring), key=lambda c: ord(c))
    return sorted_chars[10]