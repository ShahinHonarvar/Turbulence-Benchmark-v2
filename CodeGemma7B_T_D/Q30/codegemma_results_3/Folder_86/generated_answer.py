def insert_before_character(text):
    return text.replace('O', 'Q{}'.format(text[text.find('O'):text.find('O') + 1]))