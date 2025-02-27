def composite_nums_between_indices(numbers_list):
    if len(numbers_list) < 49 or len(numbers_list) >= 30:
        return set()
    composite_numbers = {num for num in numbers_list[30:49] if num > 1 and (not any((num % div == 0 for div in range(2, num))))}
    return composite_numbers