def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = s[:20]
    for char in s[20:51]:
        if char not in char_set:
            char_set.add(char)
            result += char
    return result + s[51:]