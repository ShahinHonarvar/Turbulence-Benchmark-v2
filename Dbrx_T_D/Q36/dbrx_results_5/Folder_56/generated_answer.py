def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[31:50] if not '/' < char < 'J']
    return s[:31] + ''.join(filtered_chars) + s[50:]