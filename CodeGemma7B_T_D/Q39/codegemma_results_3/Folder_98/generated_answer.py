def return_n_greatest_chars(distinct_chars):
    chars_ascii_dict = {}
    for char in distinct_chars:
        chars_ascii_dict[char] = ord(char)
    sorted_chars = sorted(chars_ascii_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars[:68]