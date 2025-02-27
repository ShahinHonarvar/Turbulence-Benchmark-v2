def insert_after_character(text):
    updated_text = text
    for i in range(len(text)):
        if text[i] == 'F':
            updated_text = updated_text[:i + 1] + 'u' + updated_text[i + 1:]
    return updated_text