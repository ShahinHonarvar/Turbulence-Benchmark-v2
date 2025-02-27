def return_nth_smallest_ascii(s):
    substring = s[30:71]
    return sorted(substring, key=lambda x: ord(x))[14]