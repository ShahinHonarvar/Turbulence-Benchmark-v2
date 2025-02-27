def filter_chars(s: str) -> str:
    start_index = 43
    end_index = 83
    char_range = range(ord(':') + 1, ord('Q'))
    for char_index in range(start_index, end_index):
        if ord(s[char_index]) in char_range:
            s = s[:char_index] + s[char_index + 1:]
    return s