def return_nth_smallest_ascii(string):
    relevant_chars = sorted(string[25:89])
    if len(relevant_chars) >= 11:
        return relevant_chars[10]
    else:
        return None