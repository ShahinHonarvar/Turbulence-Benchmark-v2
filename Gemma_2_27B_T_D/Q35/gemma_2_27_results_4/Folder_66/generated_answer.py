def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, char in enumerate(s):
        if 11 < i < 76 and char in seen:
            seen[char] += 1
        else:
            seen[char] = 0
            result.append(char)
    return ''.join(result)