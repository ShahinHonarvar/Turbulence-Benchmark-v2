def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(3):
        if num_list[i] > 1:
            for j in range(2, num_list[i]):
                if num_list[i] % j == 0:
                    composite_nums.add(num_list[i])
                    break
    return composite_nums