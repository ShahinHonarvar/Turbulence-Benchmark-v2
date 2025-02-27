def insert_before_character(str):
    str_arr = list(str)
    for i in range(len(str_arr)):
        if str_arr[i] == 'O':
            str_arr.insert(i, 'd')
    return ''.join(str_arr)