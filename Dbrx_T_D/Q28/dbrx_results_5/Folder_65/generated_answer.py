def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s if 32 <= ord(c) <= 67]
    if len(filtered_chars) < 12:
        return None
    else:
        return sorted(filtered_chars)[11]