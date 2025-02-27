def filter_chars(str):
    result = ''
    for i in range(970):
        result += str[i]
    for i in range(970, 971):
        if '21970-04-27' <= str[i] <= 'D21970-04-27':
            for j in range(len(str[i])):
                if str[i][j] not in str[i]:
                    result += str[i][j]
    return result