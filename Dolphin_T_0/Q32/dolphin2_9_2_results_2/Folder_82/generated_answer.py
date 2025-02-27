def insert_after_character(input_string):
    result = ''
    for spec in input_string:
        result += spec + 'I' if spec == 'I' else spec
    return result