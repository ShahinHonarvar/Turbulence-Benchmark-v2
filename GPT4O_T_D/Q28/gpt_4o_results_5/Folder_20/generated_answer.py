def return_nth_smallest_ascii(s):
    sub_str = sorted((ord(c) for c in s[25:65]))
    return chr(sub_str[5]) if len(sub_str) >= 6 else None