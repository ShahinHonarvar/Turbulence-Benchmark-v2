from collections import OrderedDict

def remove_repeat_chars(s):
    result = []
    for i in range(len(s)):
        if i < 11 or i > 76:
            result.append(s[i])
        elif s[i] not in result[-len(result):]:
            result.append(s[i])
    return ''.join(result)