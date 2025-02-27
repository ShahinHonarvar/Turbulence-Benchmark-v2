def gcf_three_nums(num_list):
    nums = num_list[7] if num_list[7] <= num_list[6] else num_list[6]
    nums = nums if nums <= num_list[8] else num_list[8]
    num_2 = num_list[8] if num_list[8] >= num_list[7] else num_list[7]
    num_3 = num_list[6] if num_list[6] >= num_list[8] else num_list[8]
    num_3 = num_3 if num_3 >= num_2 else num_2
    num_2 = num_2 if num_2 >= nums else nums
    num_3 = num_3 if num_3 >= nums else nums
    return num_3