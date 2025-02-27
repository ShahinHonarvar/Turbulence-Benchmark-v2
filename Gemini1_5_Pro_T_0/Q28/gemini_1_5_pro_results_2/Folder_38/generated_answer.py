def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[:46])
    if len(relevant_chars) >= 10:
        return relevant_chars[9]
    else:
        return None