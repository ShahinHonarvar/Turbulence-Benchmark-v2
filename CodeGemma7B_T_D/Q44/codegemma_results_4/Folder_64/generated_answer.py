def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(5):
        if num_list[i] != 1 and num_list[i] % 2 != 0:
            for j in range(3, int(num_list[i] ** 0.5) + 1, 2):
                if num_list[i] % j == 0:
                    composite_nums.add(num_list[i])
                    break
    return composite_nums