def filter_chars(input_str: str) -> str:
    filtered_str = ''
    for i in range(len(input_str)):
        if i >= 55 and i < 84:
            if input_str[i] > ';' and input_str[i] < 'z':
                continue
        filtered_str += input_str[i]
    return filtered_str