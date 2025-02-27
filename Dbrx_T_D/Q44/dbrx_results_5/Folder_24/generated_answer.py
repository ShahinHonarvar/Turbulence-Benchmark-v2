def composite_nums_between_indices(num_list):
    composite_nums = {i for i in num_list[34:56] if i > 1 and (not all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))))}
    return composite_nums