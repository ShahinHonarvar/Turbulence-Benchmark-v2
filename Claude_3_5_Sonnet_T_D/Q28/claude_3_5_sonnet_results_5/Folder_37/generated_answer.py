def return_nth_smallest_ascii(string):
    subset = string[28:68]
    sorted_chars = sorted(set(subset), key=ord)
    if len(sorted_chars) >= 15:
        return sorted_chars[14]
    else:
        return None