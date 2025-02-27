def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for char in s[1:11]:
        if char not in char_set:
            char_set.add(char)
            result.append(char)
    return ''.join(result) + s[11:]