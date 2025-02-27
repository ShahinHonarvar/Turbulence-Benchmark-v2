def composite_nums_between_indices(numbers):
    return {num for num in numbers[314:348] if num > 1 and any((num % div == 0 for div in range(2, num)))}