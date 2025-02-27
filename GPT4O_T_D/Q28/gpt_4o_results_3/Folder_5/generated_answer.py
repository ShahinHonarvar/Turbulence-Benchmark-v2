def return_nth_smallest_ascii(s):
    sub_string = s[5:90]
    sorted_characters = sorted(sub_string)
    return sorted_characters[12] if len(sorted_characters) >= 13 else None