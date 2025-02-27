def composite_nums_between_indices(num_list):
    return {num for num in num_list[20:31] if num > 1 and (not all((num % factor for factor in range(2, num))))}