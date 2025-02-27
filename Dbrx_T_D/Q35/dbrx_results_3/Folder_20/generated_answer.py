def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for char in s[27:96:2]}
    chars_to_remove.update((char for char in s[28:96:2]))
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)