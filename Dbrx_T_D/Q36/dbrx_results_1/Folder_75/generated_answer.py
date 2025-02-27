def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if ord('&') >= ord(char) > ord(s[46:75]) or ord('M') <= ord(char) < ord(s[46:75])]
    return ''.join(filtered_chars)