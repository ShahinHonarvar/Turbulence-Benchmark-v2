def composite_nums_between_indices(num_list):
    composite_nums = set()
    for num in num_list[262:747]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums