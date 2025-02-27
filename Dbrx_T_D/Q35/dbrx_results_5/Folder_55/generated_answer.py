def remove_repeat_chars(s: str) -> str:
    seen = set()
    chars_to_remove = set()
    result = []
    for i in range(len(s)):
        if i >= 10 and i < 100:
            if s[i] in seen:
                chars_to_remove.add(s[i])
            else:
                seen.add(s[i])
        else:
            result.append(s[i])
    for char in result:
        if char not in chars_to_remove:
            seen.remove(char)
    for char in seen:
        while char in result:
            result.remove(char)
    return ''.join(result)