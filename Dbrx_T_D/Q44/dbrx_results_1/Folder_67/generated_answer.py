def composite_nums_between_indices(numbers):
    return {num for num in numbers[56:83] if num > 1 and (not all((num % i for i in range(2, num))))}