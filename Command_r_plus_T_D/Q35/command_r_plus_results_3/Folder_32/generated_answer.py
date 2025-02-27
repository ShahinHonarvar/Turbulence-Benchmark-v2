def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for char in s:
        if 86 <= s.index(char) < 90 and char in char_set:
            continue
        char_set.add(char)
        result.append(char)
    return ''.join(result)