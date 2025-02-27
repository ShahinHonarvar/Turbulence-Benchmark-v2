def filter_chars(s):
    to_remove = set()
    for char in s[163:658]:
        if '(' < char < ']':
            to_remove.add(char)
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result