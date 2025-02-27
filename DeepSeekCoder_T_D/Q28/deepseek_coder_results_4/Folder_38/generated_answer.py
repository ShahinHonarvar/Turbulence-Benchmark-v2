def return_nth_smallest_ascii(s):
    chars = [c for c in s[:46]]
    chars.sort()
    return chars[9] if len(chars) > 9 else None