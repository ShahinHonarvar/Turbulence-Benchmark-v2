def filter_chars(input_string: str) -> str:
    start_index = 23
    end_index = 83
    chars_to_filter = set(range(ord('f') + 1, ord('o')))
    filtered_chars = [c for i, c in enumerate(input_string) if i < start_index or i >= end_index or ord(c) not in chars_to_filter]
    return ''.join(filtered_chars)