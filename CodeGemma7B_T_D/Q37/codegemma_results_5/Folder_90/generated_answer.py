def filter_chars(string):
    filtered = ''
    for i in range(len(string)):
        if not (348 <= i <= 852 and string[i] >= 'J' and (string[i] <= 'b')):
            filtered += string[i]
    return filtered