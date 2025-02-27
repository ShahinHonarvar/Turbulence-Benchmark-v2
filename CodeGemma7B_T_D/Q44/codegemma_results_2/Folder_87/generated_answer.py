def composite_nums_between_indices(num_list):
    return {num for num in num_list[43:52] if num != 1 and num != 2 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))}