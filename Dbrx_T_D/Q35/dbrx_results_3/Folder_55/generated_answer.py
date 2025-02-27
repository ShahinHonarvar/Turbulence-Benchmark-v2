def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[10:100])
    result = s[:10]
    for char in s[10:100]:
        if char not in chars_to_remove:
            result += char
        else:
            chars_to_remove.remove(char)
    return result + s[100:]