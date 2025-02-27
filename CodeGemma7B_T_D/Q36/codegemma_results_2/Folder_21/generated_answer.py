def filter_chars(string):
    result = ''
    for index in range(len(string)):
        if index >= 219 and index < 403:
            char = string[index]
            if char > '*' and char < '7':
                continue
        result += string[index]
    return result