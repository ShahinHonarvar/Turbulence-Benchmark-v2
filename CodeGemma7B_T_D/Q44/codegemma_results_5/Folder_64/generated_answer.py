def composite_nums_between_indices(num_list):
    composite_nums = set()
    for num in num_list[0:4 + 1]:
        if num % 2 == 0 or num % 3 == 0:
            composite_nums.add(num)
    return composite_nums