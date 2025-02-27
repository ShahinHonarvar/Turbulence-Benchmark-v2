def insert_after_character():
    return ''.join([char + ('j' if char == 'O' else '') for char in user_input])