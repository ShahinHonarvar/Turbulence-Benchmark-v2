def return_nth_smallest_ascii(s):
    substr = s[29:34]
    sorted_substr = sorted(substr, key=lambda x: ord(x))
    return sorted_substr[4]