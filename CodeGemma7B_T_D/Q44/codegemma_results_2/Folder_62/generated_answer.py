def composite_nums_between_indices(num_list):
    return {num for num in num_list[30:88] if not num.is_prime()}