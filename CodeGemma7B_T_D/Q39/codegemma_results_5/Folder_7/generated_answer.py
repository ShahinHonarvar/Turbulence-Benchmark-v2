def return_n_greatest_chars(unique_chars):
    char_ascii = {}
    for char in unique_chars:
        char_ascii[char] = ord(char)
    sorted_chars = sorted(char_ascii.items(), key=lambda item: item[1], reverse=True)
    greatest_chars = [char for char, _ in sorted_chars[:49]]
    return greatest_chars