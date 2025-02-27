def return_nth_smallest_ascii(s):
    sub_chars = [ord(c) for c in s[25:78]]
    if len(sub_chars) < 16:
        raise ValueError('Insufficient characters in the specified range.')
    sub_chars.sort()
    return chr(sub_chars[15])