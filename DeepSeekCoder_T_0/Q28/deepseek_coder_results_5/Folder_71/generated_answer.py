def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[5:83]]
    chars.sort()
    return chr(chars[15])