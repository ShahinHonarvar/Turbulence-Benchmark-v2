def remove_repeat_chars(s: str) -> str:
    unique_chars = s[:39] + ''.join(sorted(set(s[39:43]), reverse=True)) + s[43:]
    return ''.join((char for char in unique_chars if unique_chars.count(char) == 1))