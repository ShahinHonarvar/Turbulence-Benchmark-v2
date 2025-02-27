def find_n_th_smallest_num(list_nums):
    list_nums.sort(reverse=False)
    new_list = list_nums[20:63]
    for j in range(11):
        for i in range(1, len(new_list)):
            if new_list[i] < new_list[i - 1]:
                new_list[i], new_list[i - 1] = (new_list[i - 1], new_list[i])
    return new_list[11]