def insert_after_character(s):
    result = ''
    for c in s:
        result += c + ('a' if c == 'a' else '')
    return result