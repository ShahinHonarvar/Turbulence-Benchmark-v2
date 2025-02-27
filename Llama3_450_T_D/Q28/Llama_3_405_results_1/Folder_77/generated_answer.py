def return_nth_smallest_ascii(s):
    substr = s[63:77]
    sorted_substr = sorted(substr, key=lambda c: ord(c))
    return sorted_substr[13]