def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list) or any((not isinstance(num, int) or num < 1 for num in numbers)):
        raise ValueError('Argument must be a list of positive integers.')
    composite_numbers = set(filter(lambda num: num > 1 and (not (num & 1 and num % 3 == 0)) and all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))), numbers[22:51]))
    return composite_numbers