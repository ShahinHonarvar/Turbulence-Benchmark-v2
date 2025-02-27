def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s if 32 <= ord(c) <= 67]
    sorted_chars = sorted(filtered_chars, key=ord)
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]