def composite_nums_between_indices(input_list):
    composite_numbers = set()
    for num in input_list[:3]:
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            composite_numbers.add(num)
    return composite_numbers