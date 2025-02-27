def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('-'), ord('D') + 1)]
    filtered_s = ''.join([char for idx, char in enumerate(s) if idx < 770 or idx > 970 or char not in chars_to_remove])
    return filtered_s