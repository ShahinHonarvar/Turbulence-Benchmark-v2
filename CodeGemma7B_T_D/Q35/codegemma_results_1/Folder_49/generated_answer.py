def remove_repeat_chars(str):
    seen = set()
    result = []
    for char in str:
        if 90 < ord(char) < 200 and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)