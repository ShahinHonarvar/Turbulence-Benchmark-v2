def return_nth_smallest_ascii(input_string):
    substring = input_string[67:78]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[6]