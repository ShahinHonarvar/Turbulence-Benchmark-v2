import string

def return_nth_smallest_ascii(s):
    lowercase = string.ascii_lowercase
    idx_list = [lowercase.index(c) for c in s if c in lowercase and 37 <= s.index(c) <= 59]
    return s[min(idx_list)]