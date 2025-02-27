def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 90 or i >= 97:
            result.append(s[i])
        elif ord(s[i]) > ord('j') and ord(s[i]) < ord('w'):
            continue
        else:
            result.append(s[i])
    return ''.join(result)