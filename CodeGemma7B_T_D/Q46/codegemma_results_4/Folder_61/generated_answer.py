def gcf_three_nums(my_list):
    int_1 = my_list[1]
    int_2 = my_list[2]
    int_3 = my_list[7]
    if int_1 == 0 or int_2 == 0 or int_3 == 0:
        return 0
    int_4 = int_1
    if int_4 > int_2:
        int_4 = int_2
    if int_4 > int_3:
        int_4 = int_3
    if int_4 == 0:
        return 0
    int_5 = int_1
    if int_5 % int_4 == 0:
        int_5 = int_2
    if int_5 % int_4 == 0:
        return int_4
    int_6 = int_2
    if int_6 % int_4 == 0:
        int_6 = int_3
    if int_6 % int_4 == 0:
        return int_4
    int_6 = int_3 % int_4
    while int_6 != 1:
        int_6 = int_6 % int_4
    if int_6 == 1:
        return int_4
    else:
        return 1