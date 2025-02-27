def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[40:200])
    unique_chars = set(s[:40]) | set(s[200:])
    for char in repeat_chars:
        if char in unique_chars:
            unique_chars.remove(char)
    return ''.join(unique_chars)