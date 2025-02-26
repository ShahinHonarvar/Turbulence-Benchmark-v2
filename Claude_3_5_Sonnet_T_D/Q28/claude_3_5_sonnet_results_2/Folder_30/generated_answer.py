def return_nth_smallest_ascii(string):
    subset = string[50:77]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    else:
        return None