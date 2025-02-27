def insert_after_character(s):
    results = []
    for character in s:
        if character == ' ':
            results.append(character)
            results.append('H')
        else:
            results.append(character)
    return ''.join(results)