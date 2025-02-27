def composite_nums_between_indices(num_list):
    composite_nums = {num for num in num_list[29:94] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_nums