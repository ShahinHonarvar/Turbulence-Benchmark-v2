def return_nth_smallest_ascii(strng):
    sorted_chars = sorted(strng[8:66], key=ord)
    return sorted_chars[5]