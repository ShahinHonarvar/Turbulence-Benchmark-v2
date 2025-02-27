def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[14:75] if not '9' < char < 'K']
    return s[:14] + ''.join(filtered_chars) + s[75:]