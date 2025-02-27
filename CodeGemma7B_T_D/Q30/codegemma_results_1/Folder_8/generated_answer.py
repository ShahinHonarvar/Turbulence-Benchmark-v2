def insert_before_character(text):
    output = ''
    for char in text:
        if char == 'E' and output:
            output += 'T'
        output += char
    return output