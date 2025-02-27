def filter_chars(word):
    result = []
    for i in range(len(word)):
        if i >= 35 and i <= 89 and (ord(word[i]) >= ord('E')) and (ord(word[i]) <= ord('t')):
            continue
        result.append(word[i])
    return ''.join(result)