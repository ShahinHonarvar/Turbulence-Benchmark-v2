def return_nth_smallest_ascii(s):
    chars = [chr(i) for i in range(ord(s[46]), ord(s[72]) + 1)]
    chars.sort()
    return chars[14]