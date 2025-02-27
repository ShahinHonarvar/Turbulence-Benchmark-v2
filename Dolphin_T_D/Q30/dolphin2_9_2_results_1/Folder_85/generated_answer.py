def insert_before_character(s):
    return 'a' + ''.join([x + y for x, y in zip(['a' if y == 'o' else y for y in s], s + ' ')])