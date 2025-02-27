def return_nth_smallest_ascii(s):
    filtered_chars = s[51:79]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[8]