def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i < 75 or i > 99 or (not ord('8') <= ord(s[i]) <= ord('e')):
            result.append(s[i])
    return ''.join(result)