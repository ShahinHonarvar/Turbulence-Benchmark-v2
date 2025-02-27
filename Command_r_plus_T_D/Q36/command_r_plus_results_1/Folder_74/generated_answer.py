def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(34, 37) if i > 34 and i < 65]
    filtered_string = ''.join([char for char in s if char not in chars_to_remove])
    return filtered_string