def return_nth_smallest_ascii(s):
    sub = s[3:53]
    asc = {char: ord(char) for char in sub}
    asc_sorted = sorted(asc.items(), key=lambda x: x[1])
    return asc_sorted[7][0]