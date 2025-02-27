def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('g'), ord('o'))}
    result = []
    for index, char in enumerate(s):
        if index > 23 and index < 83 and (char in to_remove):
            continue
        result.append(char)
    return ''.join(result)