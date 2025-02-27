def return_nth_smallest_ascii(s):
    if len(s) < 5:
        return None
    selected_chars = s[:5]
    sorted_chars = sorted(selected_chars, key=lambda x: ord(x))
    return sorted_chars[4]