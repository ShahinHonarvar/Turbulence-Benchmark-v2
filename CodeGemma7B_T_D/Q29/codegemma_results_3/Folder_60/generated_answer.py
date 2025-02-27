def gcf_two_nums(num_list):
    greater_num = max(num_list[28], num_list[53])
    smaller_num = min(num_list[28], num_list[53])
    while smaller_num != 0:
        greater_num, smaller_num = (smaller_num, greater_num % smaller_num)
    return greater_num