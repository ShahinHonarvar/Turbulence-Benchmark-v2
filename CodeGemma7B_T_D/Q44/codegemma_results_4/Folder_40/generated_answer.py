def composite_nums_between_indices(num_list):
    return {num for num in num_list[2:3] if not (num == 1 or num == 2) and num % 2 != 0 or num % 3 != 0 or num % 5 != 0 or (num % 7 != 0)}