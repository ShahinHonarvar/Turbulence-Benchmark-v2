def insert_before_character(str):
    new_str = str
    for i in range(len(str)):
        if str[i] == 'A':
            new_str = new_str[:i] + 'H' + new_str[i:]
    return new_str