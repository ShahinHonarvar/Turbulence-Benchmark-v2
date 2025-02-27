def composite_nums_between_indices(int_list):
    composite_nums = set()
    for i in range(75, 89):
        if int_list[i] % 2 == 0 or int_list[i] % 3 == 0:
            composite_nums.add(int_list[i])
    return composite_nums