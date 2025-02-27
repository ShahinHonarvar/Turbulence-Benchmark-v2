def filter_chars(text):
    output = ''
    for index, char in enumerate(text):
        if 2 <= index <= 3 and char.lower() >= '5' and (char.lower() <= '_'):
            continue
        else:
            output += char
    return output