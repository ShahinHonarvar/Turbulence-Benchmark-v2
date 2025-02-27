def remove_repeat_chars(s: str) -> str:
    result = []
    char_set = set()
    for char in s:
        if char in char_set and 10 <= len(result) < 100:
            result.remove(char)
        else:
            result.append(char)
            char_set.add(char)
    return ''.join(result)