def composite_nums_between_indices(input_list):
    if len(input_list) < 2:
        return set()
    composite_numbers = {num for num in input_list[1:9] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_numbers