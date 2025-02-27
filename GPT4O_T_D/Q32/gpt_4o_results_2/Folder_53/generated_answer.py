def insert_after_character(s):
    return ''.join([char + 'I' if char == 'i' else char for char in s])