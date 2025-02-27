def remove_repeat_chars(s: str) -> str:
    char_set = set()
    non_repeat_chars = []
    for i in range(min(10, len(s)), min(79, len(s))):
        if s[i] in char_set and s[i] not in non_repeat_chars[-(len(s) - i):]:
            continue
        char_set.add(s[i])
        non_repeat_chars.append(s[i])
    return ''.join(non_repeat_chars + list(s[79:]))