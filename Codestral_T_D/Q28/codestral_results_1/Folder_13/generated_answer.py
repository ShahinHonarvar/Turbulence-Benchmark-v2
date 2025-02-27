def return_nth_smallest_ascii(s):
    substring = s[47:81]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[3]