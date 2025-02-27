def return_vowels(param_0):
    list = []
    for i in range(12, param_0.index('|')):
        for j in param_0[i:param_0.index('|')]:
            if j == ',' or j == ';' or j == '\\\\':
                continue
            elif j in ['a', 'e', 'i', 'o', 'u']:
                list.append(j)
    return list