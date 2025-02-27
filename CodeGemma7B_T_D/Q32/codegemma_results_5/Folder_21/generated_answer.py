def insert_after_character(str):
    cleaned_str = str.replace('K', '')
    result = ''
    for char in cleaned_str:
        if char == ' ':
            result += char + 'K'
        else:
            result += char
    return result