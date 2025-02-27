def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (722 <= s.index(char) <= 832 and 'K' <= char <= 'm')]
    return ''.join(filtered_chars)