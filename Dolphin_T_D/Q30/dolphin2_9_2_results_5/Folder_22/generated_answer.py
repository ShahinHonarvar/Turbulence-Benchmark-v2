def insert_before_character(text: str) -> str:
    result = ''
    for i in range(len(text)):
        if i > 0 and text[i] == 'U':
            result += text[:i] + 'U' + text[i:]
        else:
            result += text[i]
    return result