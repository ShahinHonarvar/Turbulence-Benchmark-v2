def remove_repeat_chars(s: str) -> str:
    unique_chars = set()
    result = []
    for char in s:
        if 33 < s.index(char) < 78:
            if char in unique_chars:
                continue
            else:
                unique_chars.add(char)
        result.append(char)
    return ''.join(result)