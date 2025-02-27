def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for char in s:
        if 20 <= len(result) < 200:
            if char in char_set:
                continue
            char_set.add(char)
        result.append(char)
    return ''.join(result)