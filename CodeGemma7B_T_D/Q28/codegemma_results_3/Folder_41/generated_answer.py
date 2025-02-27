def return_nth_smallest_ascii(s):
    return sorted([ch for ch in s[58:86] if ch.isalpha()], key=ord)[18]