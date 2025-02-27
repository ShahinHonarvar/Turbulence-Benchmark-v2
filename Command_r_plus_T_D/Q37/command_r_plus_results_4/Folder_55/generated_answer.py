def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if c < '$' or c > ';']
    filtered_chars.extend((c for c in s[1:6] if c < '$' or c > ';'))
    return ''.join(filtered_chars)