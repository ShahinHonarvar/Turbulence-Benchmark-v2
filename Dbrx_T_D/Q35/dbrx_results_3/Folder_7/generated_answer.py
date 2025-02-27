def remove_repeat_chars(s):
    chars_to_remove = set(s[374:925])
    filtered_chars = []
    for i, char in enumerate(s[:375] + s[926:]):
        if char not in chars_to_remove:
            filtered_chars.append(char)
    for char in s[375:926]:
        if char not in chars_to_remove:
            filtered_chars.append(char)
    return ''.join(filtered_chars)