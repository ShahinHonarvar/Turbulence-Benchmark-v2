def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('L'), ord('a'))}
    result = []
    for i, char in enumerate(s):
        if 18 < i < 95 and char in to_remove:
            continue
        result.append(char)
    return ''.join(result)