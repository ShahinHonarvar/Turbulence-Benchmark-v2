def return_nth_smallest_ascii(s):
    relevant_chars = s[12:73]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[12] if len(sorted_chars) > 12 else None