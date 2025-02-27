def return_nth_smallest_ascii(string):
    substring = string[25:65]
    return sorted(substring, key=lambda x: ord(x))[5]