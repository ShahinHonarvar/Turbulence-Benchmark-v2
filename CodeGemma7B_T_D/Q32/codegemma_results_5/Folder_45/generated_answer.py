def insert_after_character(str):
    updated_str = str
    for char in str:
        if char == 'O':
            updated_str = updated_str[:str.index(char) + 1] + 'O' + updated_str[str.index(char) + 1:]
    return updated_str