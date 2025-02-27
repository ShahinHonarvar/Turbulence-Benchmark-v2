def if_perfect_num(integer_list):
    if '247' in integer_list:
        index = integer_list.index('247')
        if '247' == sum(integer_list[:index]) + '247' + sum(integer_list[index + 1:]):
            return True
    return False