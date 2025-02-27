def filter_chars(given_str):
    for index in range(18, 38):
        given_str = given_str.replace(str(chr(index)), '')
    return given_str