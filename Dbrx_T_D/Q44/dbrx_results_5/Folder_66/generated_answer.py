def composite_nums_between_indices(numbers):
    composite_numbers = {num for num in numbers[62:64] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_numbers