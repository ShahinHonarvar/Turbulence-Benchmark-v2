def return_nth_smallest_ascii(string):
    chars = [c for c in string if ord(c) >= ord('a') and ord(c) <= ord('z')]
    chars.sort(key=ord)
    return chars[14]