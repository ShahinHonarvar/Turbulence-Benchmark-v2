def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for char in s[1:7]:
        if char in char_set:
            continue
        char_set.add(char)
        result.append(char)
    return s[:1] + ''.join(result) + s[7:]