def insert_after_character(s):
    result = ''
    for i in s:
        result += i + 'A' if i == 'A' else i
    return result