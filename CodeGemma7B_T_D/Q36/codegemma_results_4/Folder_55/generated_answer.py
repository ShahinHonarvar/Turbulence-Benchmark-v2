def filter_chars(str):
    for i in range(3, 5):
        for letter in str:
            if letter == str[i] and letter > 'Y' and (letter < 's'):
                str = str.replace(letter, '')
    return str