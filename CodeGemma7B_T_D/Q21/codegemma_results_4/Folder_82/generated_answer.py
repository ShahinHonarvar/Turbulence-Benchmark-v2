def all_ints_div_by_num(num_list):
    num_list = num_list[:3]
    for i in range(len(num_list)):
        if num_list[i] % 3 == 0:
            divisible_by_num = num_list[i]
            divisible_by_num_list.append(divisible_by_num)
    if not divisible_by_num_list:
        divisible_by_num_list = []
    return divisible_by_num_list