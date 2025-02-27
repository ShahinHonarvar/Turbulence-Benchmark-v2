def filter_chars(s):
    result = []
    for i in range(len(s)):
        if not (521 <= i <= 722 and chr(ord('>') <= s[i] <= ord('_'))):
            result.append(s[i])
    return ''.join(result)