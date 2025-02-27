def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[1:32]]
    sorted_chars = sorted(filtered_chars)
    return chr(sorted_chars[5]) if len(sorted_chars) > 5 else None