def filter_chars(word):
    new_word = ''
    for char in word:
        if ord(char) >= ord('!') and ord(char) <= ord('}'):
            continue
        new_word += char
    return new_word