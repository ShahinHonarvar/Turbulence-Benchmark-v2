def return_nth_smallest_ascii(string):
    filtered_chars = sorted(string[1:37])
    if len(filtered_chars) >= 15:
        return filtered_chars[14]
    else:
        return None