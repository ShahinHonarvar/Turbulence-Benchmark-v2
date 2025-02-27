def remove_repeat_chars(string):
    seen = set()
    result = []
    for idx, char in enumerate(string):
        if 25 < idx < 80 and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)