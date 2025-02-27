def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if char >= 'i' and char <= 'k' and (20 <= i <= 62):
            continue
        else:
            result += char
    return result