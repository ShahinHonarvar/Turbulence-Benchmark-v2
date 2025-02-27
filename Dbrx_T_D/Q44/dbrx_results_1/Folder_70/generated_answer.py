def composite_nums_between_indices(numbers_list):
    composite_nums = {num for num in numbers_list[32:36] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_nums