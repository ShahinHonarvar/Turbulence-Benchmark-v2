def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(30, 31):
        if num_list[i] > 1:
            for j in range(2, int(num_list[i] ** 0.5) + 1):
                if num_list[i] % j == 0:
                    composite_nums.add(num_list[i])
                    break
    return composite_nums