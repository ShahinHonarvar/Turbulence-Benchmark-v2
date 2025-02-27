def insert_before_character(text):
    return 'W'.join(('6' + i for i in text.split('6'))) + text.split('6')[-1]