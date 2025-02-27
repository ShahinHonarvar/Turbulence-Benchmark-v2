def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[2:7] if not 'h' < char < 'k']
    return s[:2] + ''.join(filtered_chars) + s[7:]