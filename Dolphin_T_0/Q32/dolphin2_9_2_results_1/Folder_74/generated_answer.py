def insert_after_character(string):
    result = ''
    for i in string:
        result += i + ' ' if i == 'T' else i
    return result.strip()