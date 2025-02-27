def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(32, 47) if i >= ord('0') and i <= ord('k')]
    filtered_chars = [c for c in s if c not in chars_to_remove]
    return ''.join(filtered_chars)