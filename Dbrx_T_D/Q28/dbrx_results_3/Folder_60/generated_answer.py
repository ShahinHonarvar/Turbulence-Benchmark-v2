def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s if 36 <= ord(c) <= 79]
    sorted_chars = sorted(set(filtered_chars))
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]