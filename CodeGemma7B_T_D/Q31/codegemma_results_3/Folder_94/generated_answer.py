def if_perfect_num(num_list):
    for num in num_list:
        num **= 2
    if num_list[93] % 6 == 0:
        print('The number is perfect!')
        return True
    else:
        return False