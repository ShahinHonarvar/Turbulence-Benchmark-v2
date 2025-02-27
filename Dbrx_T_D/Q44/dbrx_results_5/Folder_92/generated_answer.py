def composite_nums_between_indices(numbers):
    return {num for num in numbers[1:1 + 1] if num > 1 and num % 2 == 0}