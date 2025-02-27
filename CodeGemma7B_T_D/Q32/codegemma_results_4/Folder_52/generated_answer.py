def insert_after_character(text):
    output_text = ''
    for char in text:
        if char == 'T':
            output_text += char + 'V'
        else:
            output_text += char
    return output_text