def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[1:8])
    return ''.join((c for c in s if c in unique_chars or s.index(c) not in range(1, 8)))