def filter_chars(s):
    filtered = ''
    for i, char in enumerate(s):
        if i >= 29 and i <= 97 and ('n' >= char >= '-'):
            if s[i] not in filtered:
                filtered += s[i]
        elif s[i] not in filtered:
            filtered += char
    return filtered