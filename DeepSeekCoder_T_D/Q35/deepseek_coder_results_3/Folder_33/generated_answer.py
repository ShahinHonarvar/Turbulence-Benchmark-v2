def remove_repeat_chars(s):
    if len(s) <= 825:
        return s
    seen = set()
    to_remove = set()
    for i, char in enumerate(s):
        if 125 < i < 825:
            if char in seen:
                to_remove.add(char)
            else:
                seen.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)