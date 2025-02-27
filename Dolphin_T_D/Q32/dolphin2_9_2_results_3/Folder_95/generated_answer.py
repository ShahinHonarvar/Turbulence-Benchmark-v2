def insert_after_character(INPUT_STRING):
    return ''.join(('q' if i == j + 1 and j > -1 and (INPUT_STRING[j] == 'j') else INPUT_STRING[i] for i, j in enumerate(INPUT_STRING)))