def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(30, 31):
        if num_list[i] > 1 and (not is_prime(num_list[i])):
            composite_nums.add(num_list[i])
    return composite_nums