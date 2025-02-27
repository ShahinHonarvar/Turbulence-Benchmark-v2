def remove_repeat_chars(s: str) -> str:
    used_char_indices = {}
    chars_to_remove = set()
    for i, char in enumerate(s):
        if 20 <= i < 35:
            if char in used_char_indices:
                chars_to_remove.add(char)
            used_char_indices[char] = i
        elif char in chars_to_remove:
            s = s[:i] + s[i + 1:]
    return s