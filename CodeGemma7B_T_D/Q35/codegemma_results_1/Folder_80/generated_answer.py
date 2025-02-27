def remove_repeat_chars(text):
    """Iterate through the text between indices 57 and 84."""
    for char in text[57:84]:
        'Count the appearances of the character.'
        if text[57:84].count(char) > 1:
            'Remove all occurrences of the character.'
            text = ''.join(filter(lambda x: x != char, text))
            'Break out of the loop if the character is removed.'
            break
    return text