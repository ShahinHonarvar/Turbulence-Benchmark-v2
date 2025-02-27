def filter_chars(string: str) -> str:
    filtered_string = ''
    for i in range(len(string)):
        if i >= 259 and i <= 502 and (string[i] >= ',') and (string[i] <= '3'):
            continue
        filtered_string += string[i]
    return filtered_string