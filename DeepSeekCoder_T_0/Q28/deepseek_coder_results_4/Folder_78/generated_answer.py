def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(min(88, len(s)))]
    filtered_chars.sort()
    return filtered_chars[13] if len(filtered_chars) > 13 else None