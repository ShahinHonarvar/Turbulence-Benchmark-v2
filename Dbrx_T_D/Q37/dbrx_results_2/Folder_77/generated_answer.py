def filter_chars(input_string):
    chars_to_filter = set(range(ord('/'), ord('8') + 1))
    filtered_chars = [c for i, c in enumerate(input_string) if i < 384 or i > 411 or c not in chars_to_filter]
    return ''.join(filtered_chars)