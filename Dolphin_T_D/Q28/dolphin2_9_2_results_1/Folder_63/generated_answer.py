def return_nth_smallest_ascii(s):
    substring = s[47:71]
    sorted_substring = sorted(substring, key=lambda c: ord(c))
    return sorted_substring[13]