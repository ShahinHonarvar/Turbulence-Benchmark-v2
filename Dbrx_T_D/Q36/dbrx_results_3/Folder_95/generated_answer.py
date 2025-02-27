def filter_chars(s: str) -> str:
    start_index = 56
    end_index = 86
    char_range = set(range(ord('+') + 1, ord('w')))
    for i in range(start_index, end_index):
        if ord(s[i]) in char_range:
            s = s[:i] + s[i + 1:]
    return s