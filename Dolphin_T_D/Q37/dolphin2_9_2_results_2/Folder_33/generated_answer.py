def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 722 and i <= 832:
            char = s[i]
            if char >= 'K' and char <= 'm':
                continue
        result += s[i]
    return result