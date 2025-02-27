def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (32 <= ord(c) < 51 and ord(c) > ord('/'))]
    return ''.join(filtered_chars)