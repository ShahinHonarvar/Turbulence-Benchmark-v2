def return_nth_smallest_ascii(string):
    subset = string[5:90]
    sorted_chars = sorted(set(subset), key=ord)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    else:
        return None