def return_nth_smallest_ascii(s):
    selected_chars = s[22:75]
    sorted_chars = sorted(selected_chars, key=lambda x: ord(x))
    return sorted_chars[11] if len(sorted_chars) >= 12 else None