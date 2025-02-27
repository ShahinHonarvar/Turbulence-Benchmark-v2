def return_nth_smallest_ascii(s):
    chars = [c for c in s[17:57]]
    chars.sort(key=lambda x: ord(x))
    if len(chars) >= 9:
        return chars[8]
    else:
        return None