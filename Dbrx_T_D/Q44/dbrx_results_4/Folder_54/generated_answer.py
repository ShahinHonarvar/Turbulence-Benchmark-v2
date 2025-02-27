def composite_nums_between_indices(numbers):
    composite_nums = {num for num in numbers[14:65] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_nums