def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[10:80])
    repeat_chars = {char for char in repeat_chars if s.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))