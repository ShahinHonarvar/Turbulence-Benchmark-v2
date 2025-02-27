def remove_repeat_chars(s: str) -> str:
    target_range = s[306:807]
    unique_chars = set(target_range)
    chars_to_remove = set()
    for char in unique_chars:
        if target_range.count(char) > 1:
            chars_to_remove.add(char)
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result