def return_nth_smallest_ascii(s):
    extracted_chars = s[3:27]
    sorted_chars = sorted(extracted_chars)
    return sorted_chars[4]