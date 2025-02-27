def return_nth_smallest_ascii(s):
    return sorted([ch for ch in s if 17 <= ord(ch) <= 86])[14]