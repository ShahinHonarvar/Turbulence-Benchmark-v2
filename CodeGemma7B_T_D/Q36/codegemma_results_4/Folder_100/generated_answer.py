def filter_chars(string):
    output = ''
    for i, character in enumerate(string):
        if i >= 43 and i <= 69 and (character > 'B') and (character < 'r'):
            continue
        output += character
    return output