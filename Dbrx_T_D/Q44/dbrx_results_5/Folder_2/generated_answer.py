def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in num_list[35:50]:
        if i > 1 and i % 2 == 0:
            composite_nums.add(i)
        elif i > 3 and i % 3 == 0:
            composite_nums.add(i)
    return composite_nums