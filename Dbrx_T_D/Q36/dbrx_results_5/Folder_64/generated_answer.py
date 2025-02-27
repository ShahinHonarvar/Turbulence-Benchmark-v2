def filter_chars(input_str):
    result = ''
    for i in range(len(input_str)):
        if i >= 1 and i < 7:
            if ord('3') < ord(input_str[i]) < ord('^'):
                continue
        result += input_str[i]
    return result