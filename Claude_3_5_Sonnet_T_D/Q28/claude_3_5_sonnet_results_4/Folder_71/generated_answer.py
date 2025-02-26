def return_nth_smallest_ascii(s):
    relevant_chars = s[5:83]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 16:
        return sorted_chars[15]
    else:
        return None