def insert_before_character(str):
    return ''.join([i for i in str if i != '5'] + ['R'] + [i for i in str if i == '5'])