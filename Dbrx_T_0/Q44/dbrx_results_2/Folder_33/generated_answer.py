def composite_nums_between_indices(numbers):
    return {num for num in numbers[314:348] if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}