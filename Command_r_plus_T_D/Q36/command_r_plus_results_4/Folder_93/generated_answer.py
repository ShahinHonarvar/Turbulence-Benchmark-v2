def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('&') + 1, ord('c'))]
    filtered_string = ''.join([char for char in s if char not in chars_to_remove or char in s[52:88]])
    return filtered_string