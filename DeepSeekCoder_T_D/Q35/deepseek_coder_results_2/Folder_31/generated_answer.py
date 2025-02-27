def remove_repeat_chars(s):
    start, end = (33, 78)
    seen = set()
    to_remove = set()
    for i, char in enumerate(s):
        if start < i < end:
            if char in seen:
                to_remove.add(char)
            else:
                seen.add(char)
    result = ''.join((char for char in s if char not in to_remove))
    return result