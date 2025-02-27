def filter_chars(s: str) -> str:
    start_index = 344
    end_index = 874
    char_range = range(ord('f') + 1, ord('~'))
    filtered_chars = [char for i, char in enumerate(s) if i < start_index or i >= end_index or ord(char) not in char_range]
    return ''.join(filtered_chars)