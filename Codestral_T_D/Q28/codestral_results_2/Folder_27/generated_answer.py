def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s if 33 <= ord(c) <= 85]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[12] if len(sorted_chars) > 12 else None