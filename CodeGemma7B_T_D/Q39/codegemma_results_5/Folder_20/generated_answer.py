def return_n_greatest_chars(char_str):
    ascii_list = [(ord(char), char) for char in char_str]
    ascii_list.sort(reverse=True)
    return [char for _, char in ascii_list[:40]]