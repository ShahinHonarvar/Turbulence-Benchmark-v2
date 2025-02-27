def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s if 47 <= ord(c) <= 70]
    filtered_chars.sort(key=ord)
    return filtered_chars[13] if len(filtered_chars) >= 14 else None