def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[47:81])
    relevant_chars.sort(key=lambda x: ord(x))
    return relevant_chars[3]