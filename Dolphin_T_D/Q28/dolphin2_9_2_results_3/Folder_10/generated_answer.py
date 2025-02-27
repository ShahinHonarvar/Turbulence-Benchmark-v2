def return_nth_smallest_ascii(s):
    chars = s[38:83]
    ascii_vals = {char: ord(char) for char in chars}
    sorted_chars = sorted(ascii_vals.items(), key=lambda x: x[1])
    return sorted_chars[19][0]