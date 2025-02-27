def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[35:53] if ord(c) > 47 and ord(c) < 58 or (ord(c) > 64 and ord(c) < 91) or (ord(c) > 96 and ord(c) < 123)]
    filtered_chars.sort(key=ord)
    return filtered_chars[10] if len(filtered_chars) > 10 else None