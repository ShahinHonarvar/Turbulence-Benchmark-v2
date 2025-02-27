def remove_repeat_chars(s: str) -> str:
    chars_between_indices = set(s[19:32])
    altered_chars = []
    for char in s:
        if char not in chars_between_indices or s.count(char) == 1:
            altered_chars.append(char)
    return ''.join(altered_chars)