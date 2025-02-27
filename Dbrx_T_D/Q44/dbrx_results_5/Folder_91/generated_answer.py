def composite_nums_between_indices(num_list):
    if len(num_list) < 6:
        return set()
    else:
        start_index = 5
        end_index = min(5 + 5, len(num_list))
        return {num for num in num_list[start_index:end_index + 1] if num > 1 and (not all((num % i for i in range(2, num))))}