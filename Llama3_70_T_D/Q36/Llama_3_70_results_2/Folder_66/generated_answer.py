def filter_chars(s):
    result = ''
    for char in s:
        removal_needed = False
        for c in s[39:87]:
            if c > '!' and c < '}' and (char == c):
                removal_needed = True
                break
        if not removal_needed:
            result += char
    return result