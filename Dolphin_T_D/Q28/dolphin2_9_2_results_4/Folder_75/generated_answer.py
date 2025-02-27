def return_nth_smallest_ascii(s):
    sub_string = s[62:84]
    asc_dict = {char: ord(char) for char in sub_string}
    sorted_chars = sorted(asc_dict.items(), key=lambda x: x[1])
    return sorted_chars[8][0]