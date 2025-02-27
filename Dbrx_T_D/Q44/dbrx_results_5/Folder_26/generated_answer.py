def composite_nums_between_indices(input_list):
    composite_set = set()
    for i in range(22, 51):
        num = input_list[i]
        if num > 1 and all((num % j != 0 for j in range(2, num))):
            composite_set.add(num)
    return composite_set