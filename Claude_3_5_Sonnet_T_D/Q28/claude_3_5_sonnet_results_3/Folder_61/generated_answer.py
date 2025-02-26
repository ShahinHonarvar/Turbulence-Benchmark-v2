def return_nth_smallest_ascii(s):
    relevant_chars = s[:10]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None