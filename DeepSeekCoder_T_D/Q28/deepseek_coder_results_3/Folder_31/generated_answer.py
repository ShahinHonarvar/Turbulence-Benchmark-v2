def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[10:83]]
    chars.sort()
    return chr(chars[17])