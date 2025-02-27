def return_nth_smallest_ascii(s):
    substring = s[22:75]
    return sorted(substring, key=lambda x: ord(x))[11]