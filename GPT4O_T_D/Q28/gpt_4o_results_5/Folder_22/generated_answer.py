def return_nth_smallest_ascii(s):
    if len(s) < 17:
        indices_to_check = s
    else:
        indices_to_check = s[:17]
    sorted_chars = sorted(indices_to_check)
    return sorted_chars[16] if len(sorted_chars) >= 17 else None