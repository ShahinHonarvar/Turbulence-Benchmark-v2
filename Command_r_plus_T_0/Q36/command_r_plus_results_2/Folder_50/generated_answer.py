def filter_chars(s: str) -> str:
    filtered_string = ''.join([char for char in s if not 61 < ord(char) < 88 or char <= '%' or char >= 'q'])
    return filtered_string