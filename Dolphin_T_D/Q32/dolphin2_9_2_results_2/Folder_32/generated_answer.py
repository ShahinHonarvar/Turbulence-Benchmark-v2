def insert_after_character(s):
    result = ''
    for c in s:
        result += c + 'u' if c == 'F' else c
    return result