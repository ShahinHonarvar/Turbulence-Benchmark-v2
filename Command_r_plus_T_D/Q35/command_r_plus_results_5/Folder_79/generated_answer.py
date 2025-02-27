def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[1:8])
    result = [char for i, char in enumerate(s) if i == 0 or char in unique_chars]
    return ''.join(result)