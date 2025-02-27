from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    if len(s) < 50 or len(s) < 200:
        return s
    chars = set(s[50:200])
    result = []
    for i in range(len(s)):
        if i < 50 or i > 199 or s[i] not in chars:
            result.append(s[i])
    return ''.join(result)