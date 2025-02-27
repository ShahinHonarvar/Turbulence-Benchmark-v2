def gcf_three_nums(num_list):
    gcf = num_list[404]
    for i in range(404, 835):
        if num_list[i] % num_list[517] == 0 and num_list[i] % num_list[834] == 0:
            gcf = num_list[i]
    return gcf