def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[18:60])
    new_s = ''.join((char for char in s if char not in unique_chars or s[:18] + s[60:] + char not in s))
    return new_s