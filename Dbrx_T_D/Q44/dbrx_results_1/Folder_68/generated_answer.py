def composite_nums_between_indices(numbers):
    return {num for num in set(numbers[0:9]) if num > 1 and num % 2 == 0}