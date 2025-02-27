def return_nth_smallest_ascii(s):
    filtered_chars = [ord(s[i]) for i in range(6, min(59, len(s)))]
    filtered_chars.sort()
    return chr(filtered_chars[18]) if len(filtered_chars) >= 19 else None