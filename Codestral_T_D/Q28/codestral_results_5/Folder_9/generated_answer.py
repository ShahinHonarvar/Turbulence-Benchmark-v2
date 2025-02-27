def return_nth_smallest_ascii(s):
    filtered_chars = s[10:91]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[19]