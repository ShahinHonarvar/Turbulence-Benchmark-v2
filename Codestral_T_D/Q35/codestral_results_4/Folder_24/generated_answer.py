def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    result = []
    for i, char in enumerate(s):
        if 13 < i < 91:
            if char in seen and char not in repeat:
                repeat.add(char)
            else:
                seen.add(char)
        if char not in repeat:
            result.append(char)
    return ''.join(result)