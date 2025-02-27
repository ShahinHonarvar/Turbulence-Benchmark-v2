from collections import OrderedDict

def remove_repeat_chars(s):
    if len(s) <= 80:
        return s
    result = OrderedDict()
    for i in range(0, 10):
        result[s[i]] = 1
    for i in range(10, 79):
        if s[i] not in result:
            result[s[i]] = 1
        else:
            result[s[i]] += 1
    for i in range(79, len(s)):
        if s[i] not in result:
            result[s[i]] = 1
        else:
            result[s[i]] += 1
    return ''.join((char for char, count in result.items() if count == 1))