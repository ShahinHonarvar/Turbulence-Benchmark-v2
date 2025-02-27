def filter_chars(input_string: str) -> str:
    filtered_string = input_string[:54] + input_string[54:84].replace('j', '').replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '') + input_string[84:]
    return filtered_string