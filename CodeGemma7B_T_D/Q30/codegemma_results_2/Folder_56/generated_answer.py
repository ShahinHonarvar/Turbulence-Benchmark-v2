def insert_before_character(txt_spec):
    if 'I' in txt_spec:
        for index, letter in enumerate(txt_spec):
            if letter == 'I':
                txt_spec = txt_spec[:index] + 'i' + txt_spec[index:]
    return txt_spec