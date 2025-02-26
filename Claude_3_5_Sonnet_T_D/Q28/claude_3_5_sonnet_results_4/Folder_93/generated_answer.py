def return_nth_smallest_ascii(s):
    relevant_chars = s[42:60]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 17:
        return sorted_chars[16]
    else:
        return None