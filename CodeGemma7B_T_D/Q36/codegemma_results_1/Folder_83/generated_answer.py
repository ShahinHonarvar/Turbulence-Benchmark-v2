def filter_chars(target):
    for i in range(72, 93):
        if target[i] > '<' and target[i] < 'J':
            for j in range(i + 1, len(target)):
                if target[j] == target[i]:
                    target[j] = '_'
    return target.replace('_', '')