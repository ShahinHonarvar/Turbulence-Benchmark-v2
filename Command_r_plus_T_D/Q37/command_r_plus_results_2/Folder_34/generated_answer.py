def filter_chars(s: str) -> str:
    filtered_chars = [')', '(', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return ''.join((c for c in s if c not in filtered_chars or 54 <= s.index(c) <= 62))