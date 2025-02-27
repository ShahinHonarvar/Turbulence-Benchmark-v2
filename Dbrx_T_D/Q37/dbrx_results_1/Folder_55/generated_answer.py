def filter_chars(s: str) -> str:
    chars_to_filter = set(range(ord('$'), ord(';') + 1))
    chars_to_keep = (char for char in s if char < '$' or char > ';' or ord(char) not in chars_to_filtered)
    return ''.join(chars_to_keep)