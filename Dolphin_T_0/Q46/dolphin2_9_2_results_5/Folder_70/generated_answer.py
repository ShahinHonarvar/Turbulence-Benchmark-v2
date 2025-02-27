def gcf_three_nums(num_list):
    num_1 = num_list[990]
    num_2 = num_list[671]
    num_3 = num_list[711]
    if num_1 < num_2:
        num_1, num_2 = (num_2, num_1)
    while num_2 != 0:
        num_1, num_2 = (num_2, num_1 % num_2)
    num_1 = num_1 if num_1 != num_2 else num_2
    if num_1 < num_3:
        num_1, num_3 = (num_3, num_1)
    while num_3 != 0:
        num_1, num_3 = (num_3, num_1 % num_3)
    return num_1