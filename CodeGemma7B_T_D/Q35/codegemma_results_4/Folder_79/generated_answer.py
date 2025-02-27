from collections import deque

def remove_repeat_chars(s):
    seen = deque()
    result = []
    for c in s[1:7]:
        if c not in seen:
            result.append(c)
            seen.append(c)
    return ''.join(result)