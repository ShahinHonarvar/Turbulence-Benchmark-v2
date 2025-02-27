def return_nth_smallest_ascii(s):
    sub_s = [ch for ch in s if 48 <= ord(ch) <= 76]
    sub_s.sort()
    return sub_s[4]