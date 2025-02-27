def insert_before_character(string):
    for i, char in enumerate(string):
        if char == 'H':
            return string[:i] + 's' + string[i:]