def filter_chars(s):
    removal_set = set((chr(i) for i in range(ord('#') + 1, ord('L'))))
    result = []
    for index, char in enumerate(s):
        if index <= 69 or index >= 87 or char not in removal_set:
            result.append(char)
    return ''.join(result)