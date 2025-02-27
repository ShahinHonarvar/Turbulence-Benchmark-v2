def insert_before_character(text):
    return 'F'.join(('U' not in [x, text[i + 1]] and [x] or [x, 'F'] for i, x in enumerate(text)))