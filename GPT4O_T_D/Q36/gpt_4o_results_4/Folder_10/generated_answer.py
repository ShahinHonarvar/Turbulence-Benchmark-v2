def filter_chars(input_string):
    if len(input_string) <= 35:
        return input_string
    start_index = 36
    end_index = min(60, len(input_string))
    chars_to_remove = [ch for ch in input_string[start_index:end_index] if '!' < ch < 'B']
    return ''.join((ch for ch in input_string if ch not in chars_to_remove))