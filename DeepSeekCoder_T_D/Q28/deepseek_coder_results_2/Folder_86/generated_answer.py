def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[44:70]]
    chars.sort()
    return chr(chars[14])