def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, c in enumerate(s):
        if 51 <= i < 76:
            if c in char_set:
                continue
            else:
                char_set.add(c)
        result.append(c)
    return ''.join(result)