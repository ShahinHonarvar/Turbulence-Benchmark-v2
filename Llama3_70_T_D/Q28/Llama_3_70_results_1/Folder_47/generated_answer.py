def return_nth_smallest_ascii(s):
    substring = s[3:53]
    sorted_ascii = sorted(set(substring))
    return sorted_ascii[7]