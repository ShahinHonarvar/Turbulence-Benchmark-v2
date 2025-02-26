def return_nth_smallest_ascii(s):
    relevant_chars = s[17:66]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 8:
        return sorted_chars[7]
    else:
        return None