def composite_nums_between_indices(numbers):
    return {num for num in numbers[2:4] if num > 1 and num % 2 == 0}