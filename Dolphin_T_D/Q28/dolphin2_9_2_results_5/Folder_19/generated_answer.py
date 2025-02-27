def return_nth_smallest_ascii(s):
    chars = s[0:19]
    asc_values = list(map(lambda c: ord(c), chars))
    asc_values.sort()
    return chars[asc_values.index(asc_values[12])]