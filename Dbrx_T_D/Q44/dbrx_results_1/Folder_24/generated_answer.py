def composite_nums_between_indices(num_list):
    return {num for num in num_list[34:56] if num > 1 and (not all((num % div for div in range(2, num))))} or set()