def remove_repeat_chars(s: str) -> str:
    unique_chars = set()
    result = []
    for char in s:
        if char not in unique_chars and 1 <= s.index(char) < 8:
            unique_chars.add(char)
            result.append(char)
    return ''.join(result)