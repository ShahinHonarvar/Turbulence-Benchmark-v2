def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 75 >= ord(c) >= 57 or 97 <= ord(c) <= 122]
    return ''.join(filtered_chars)[18:95]