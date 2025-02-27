def return_nth_smallest_ascii(txt):
    freq_ascii = {}
    for char in txt[1:47]:
        freq_ascii[char] = ord(char)
    ascii_values = sorted(freq_ascii.values())
    return chr(ascii_values[12])