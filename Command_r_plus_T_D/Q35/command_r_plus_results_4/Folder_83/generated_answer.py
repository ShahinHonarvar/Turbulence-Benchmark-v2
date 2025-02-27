def remove_repeat_chars(s: str) -> str:
    unique_chars = set()
    result = []
    for i, char in enumerate(s):
        if 100 <= i < 200:
            if char in unique_chars:
                continue
            unique_chars.add(char)
        result.append(char)
    return ''.join(result)