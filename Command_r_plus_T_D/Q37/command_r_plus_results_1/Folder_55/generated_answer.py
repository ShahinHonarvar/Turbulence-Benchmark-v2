def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if char < '$' or char > ';']
    filtered_chars.extend((char for char in s[1:6] if char < '$' or char > ';'))
    return ''.join(filtered_chars)