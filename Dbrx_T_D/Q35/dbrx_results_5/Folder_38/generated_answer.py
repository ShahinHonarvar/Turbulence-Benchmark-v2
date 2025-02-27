def remove_repeat_chars(s):
    charset = set()
    result = s[:36]
    for char in s[36:85]:
        if char not in charset:
            result += char
            charset.add(char)
    result += s[85:]
    return result