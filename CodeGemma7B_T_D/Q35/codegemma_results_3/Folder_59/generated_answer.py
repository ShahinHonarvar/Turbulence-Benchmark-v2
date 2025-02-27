def remove_repeat_chars(str):
    seen = set()
    result = []
    for char in str[0:10]:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)