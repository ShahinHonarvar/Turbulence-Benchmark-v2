def filter_chars(input_string: str) -> str:
    start_index = 14
    end_index = 75
    filtered_chars = []
    for i in range(len(input_string)):
        if i >= start_index and i < end_index:
            if ord('9') < ord(input_string[i]) < ord('K'):
                continue
        filtered_chars.append(input_string[i])
    return ''.join(filtered_chars)