def return_nth_smallest_ascii(s):
    substr = s[20:81]
    unique_chars = sorted(set(substr))
    return unique_chars[10]