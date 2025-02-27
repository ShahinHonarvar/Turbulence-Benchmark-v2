def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[100:200])
    return ''.join((c for i, c in enumerate(s) if i < 100 or c not in unique_chars))