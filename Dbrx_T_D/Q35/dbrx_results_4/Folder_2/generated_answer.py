def remove_repeat_chars(s: str) -> str:
    unique_chars = []
    for char in s[72:93]:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join((char if s[72:93].count(char) == 1 else '' for char in s))