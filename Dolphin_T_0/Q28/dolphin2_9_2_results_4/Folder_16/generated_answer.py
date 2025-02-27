def return_nth_smallest_ascii(string):
    sub_string = string[18:46]
    sorted_chars = sorted(sub_string, key=lambda x: ord(x))
    return sorted_chars[6]