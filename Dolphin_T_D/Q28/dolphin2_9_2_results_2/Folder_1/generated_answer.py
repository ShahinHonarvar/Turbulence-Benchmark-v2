def return_nth_smallest_ascii(s):
    substr = s[21:60]
    sorted_substr = sorted(set(substr), key=lambda x: ord(x))
    return sorted_substr[10]