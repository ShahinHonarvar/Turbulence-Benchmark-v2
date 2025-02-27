def filter_chars(s: str) -> str:
    to_remove = [ch for ch in s[3:9] if '*' < ch < 'E']
    new_s = [ch for ch in s if ch not in to_remove]
    return ''.join(new_s)