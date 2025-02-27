def filter_chars(s: str) -> str:
    start_index, end_index = (43, 59)
    chars_to_remove = {chr(i) for i in range(ord('5') + 1, ord('C'))} if start_index < len(s) < end_index else set()
    return ''.join((char for char in s if char not in chars_to_remove))