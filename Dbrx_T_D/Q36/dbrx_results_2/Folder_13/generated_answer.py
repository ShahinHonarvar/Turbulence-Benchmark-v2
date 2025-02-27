def filter_chars(s: str) -> str:
    start, end = (323, 526)
    filtered_chars = [c for c in s if start < s.index(c) < end and ord(')') < ord(c) < ord('O')]
    return ''.join(filtered_chars)