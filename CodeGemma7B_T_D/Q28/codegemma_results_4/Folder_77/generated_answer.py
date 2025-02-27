def return_nth_smallest_ascii(s):
    return sorted([c for c in s[63:77] if c in string.ascii_lowercase], key=ord)[-14]