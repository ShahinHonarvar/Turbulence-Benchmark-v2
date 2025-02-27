def return_nth_smallest_ascii(s):
    sub = s[18:67]
    return chr(sorted([ord(x) for x in set(sub)])[18])