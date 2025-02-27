def return_nth_smallest_ascii(s):
    substring = s[34:69]
    sorted_substring = sorted(substring, key=lambda c: ord(c))
    return sorted_substring[5]