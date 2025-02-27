def remove_repeat_chars(s: str) -> str:
    chars_between_20_and_36 = set(s[20:36])
    unique_chars = []
    for char in s:
        if char not in chars_between_20_and_36 or s.count(char) == 1:
            unique_chars.append(char)
    return ''.join(unique_chars)