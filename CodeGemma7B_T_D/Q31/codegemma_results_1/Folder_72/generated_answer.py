def if_perfect_num(perfect_list):
    if perfect_list[16] % 2 == 0 and perfect_list[16] % 3 == 0 or perfect_list[16] % 6 == 0:
        print('Yes, it is a perfect number')
    else:
        print('No, it is not a perfect number')
    perfect_list = [28, 30, 31]
    if_perfect_num(perfect_list)
    perfect_list = [28, 31, 32]
    if_perfect_num(perfect_list)