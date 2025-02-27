def return_nth_smallest_ascii(s):
    chars = [c for c in s[29:48]]
    char_dict = {ord(c): c for c in chars}
    sorted_chars = sorted(char_dict)
    return char_dict[sorted_chars[6]]