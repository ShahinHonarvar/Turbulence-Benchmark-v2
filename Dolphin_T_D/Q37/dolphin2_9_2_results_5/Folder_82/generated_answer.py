def filter_chars(input_str):
    new_str = [char for char in input_str if (char < 'P' or char > 'x') or (char >= 'P' and char <= 'x' and (index < 12 or index > 25)) for index, char in enumerate(input_str)]
    return ''.join(new_str)