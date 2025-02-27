def insert_after_character(str):
    return ''.join([x for x in str if not (x == 'o' and str[i + 1] == 'o')] + [x for x in str if x == 'o'])