def return_nth_smallest_ascii(s):
    substring = s[5:11]
    sorted_substring = [char for char in sorted(substring, key=lambda x: ord(x))]
    return sorted_substring[5]