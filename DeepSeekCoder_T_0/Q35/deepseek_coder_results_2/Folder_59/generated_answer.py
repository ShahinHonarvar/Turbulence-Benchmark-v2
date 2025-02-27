def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    seen = set()
    to_remove = set()
    for char in s[1:10]:
        if char in seen:
            to_remove.add(char)
        else:
            seen.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)