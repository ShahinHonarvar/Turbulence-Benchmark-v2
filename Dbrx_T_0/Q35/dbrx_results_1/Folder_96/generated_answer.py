def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if 60 < i < 200:
            if char in char_set:
                continue
            else:
                char_set.add(char)
        result.append(char)
    return ''.join(result)