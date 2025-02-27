def return_nth_smallest_ascii(s):
    chars = s[20:81]
    sorted_chars = sorted(chars, key=lambda char: ord(char))
    return sorted_chars[10]