def return_nth_smallest_ascii(s):
    relevant_substring = s[51:61]
    sorted_chars = sorted(relevant_substring)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None