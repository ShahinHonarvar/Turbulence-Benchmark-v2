def insert_after_character(text):
    """Inserts the letter 'I' immediately succeeding any occurrences of the letter 'I'."""
    result = []
    for i in text:
        if i == 'I':
            result.append(i)
            result.append('I')
        else:
            result.append(i)
    return ''.join(result)