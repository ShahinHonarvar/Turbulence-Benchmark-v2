def filter_chars(string):
    filtered_chars = []
    for i in range(len(string)):
        if i >= 31 and i < 73:
            if ord(string[i]) > ord('M') and ord(string[i]) < ord('j'):
                continue
        filtered_chars.append(string[i])
    filtered_string = ''.join(filtered_chars)
    return filtered_string