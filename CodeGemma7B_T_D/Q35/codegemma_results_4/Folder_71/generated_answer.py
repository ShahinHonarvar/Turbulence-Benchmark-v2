def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i in range(20, 35) and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)