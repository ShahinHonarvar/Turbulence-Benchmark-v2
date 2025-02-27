def return_nth_smallest_ascii(s):
    sub_s = s[18:67]
    sorted_chars = sorted(sub_s, key=lambda x: ord(x))
    return sorted_chars[18]