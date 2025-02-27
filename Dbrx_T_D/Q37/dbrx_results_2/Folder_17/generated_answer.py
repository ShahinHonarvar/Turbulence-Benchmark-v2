def filter_chars(input_string):
    characters_to_remove = set(input_string[27:30])
    characters_to_remove = {c for c in characters_to_remove if ord(';') <= ord(c) <= ord('b')}
    result = [c for c in input_string if c not in characters_to_remove]
    return ''.join(result)