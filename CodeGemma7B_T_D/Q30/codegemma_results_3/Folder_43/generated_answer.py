def insert_before_character(word):
    return ''.join((c + ('G' if c == 't' else '') for c in word))