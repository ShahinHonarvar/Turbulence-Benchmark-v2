def filter_chars(word):
    result = ''
    for letter in word:
        if letter > '5' and letter < 'A':
            continue
        result += letter
    return result