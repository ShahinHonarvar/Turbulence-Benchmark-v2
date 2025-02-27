def return_nth_smallest_ascii(s):
    s = ''.join(sorted([char for char in s if 32 <= ord(char) <= 67]))
    return s[11]