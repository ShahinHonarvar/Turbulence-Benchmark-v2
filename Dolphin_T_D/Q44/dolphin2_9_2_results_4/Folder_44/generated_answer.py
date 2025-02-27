def composite_nums_between_indices(num_list):
    return {num for num in num_list[64:67] if any((num % i == 0 for i in range(2, num)))}