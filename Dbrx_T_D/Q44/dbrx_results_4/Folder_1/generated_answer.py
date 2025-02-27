def composite_nums_between_indices(numbers):
    if not all((isinstance(i, int) and i > 0 for i in numbers)):
        raise ValueError('All elements in the list must be positive integers')
    composite_nums = set()
    for i in range(len(numbers)):
        if i >= 69 and i <= 83:
            num = numbers[i]
            if num > 1 and (not (num == 2 or (num % 2 == 0 and num > 2))):
                composite_nums.add(num)
    return composite_nums