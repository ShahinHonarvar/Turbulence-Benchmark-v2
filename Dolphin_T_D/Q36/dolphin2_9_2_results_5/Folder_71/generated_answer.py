def filter_chars(s):
    result = ''
    for ch in s:
        if ch > '*' and ch < '[':
            if ch not in result:
                result += ch
        else:
            result += ch
    return result