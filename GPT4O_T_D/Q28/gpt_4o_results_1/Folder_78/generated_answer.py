def return_nth_smallest_ascii(s):
    slice_end = min(len(s), 88)
    sub_string = s[:slice_end]
    sorted_characters = sorted(sub_string)
    return sorted_characters[13] if len(sorted_characters) >= 14 else None