def insert_before_character(a):
    flag = False
    result = []
    for i in a:
        if i == 'o' and flag is False:
            flag = True
            result.append('O')
        result.append(i)
    return ''.join(result)