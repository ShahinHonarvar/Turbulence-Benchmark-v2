def filter_chars(word):
    chars_to_remove = [char for i, char in enumerate(word) if 10 <= i <= 69 and 'I' <= char <= 'K']
    for char in chars_to_remove:
        word = word.replace(char, '')
    return word