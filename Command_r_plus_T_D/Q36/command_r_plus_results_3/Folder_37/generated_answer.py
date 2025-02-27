def filter_chars(s: str) -> str:
    to_remove = [chr(i) for i in range(ord('/'), ord('6'))]
    result = []
    i = 0
    while i < len(s):
        if 44 < i < 59 and s[i] in to_remove:
            i += 1
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)