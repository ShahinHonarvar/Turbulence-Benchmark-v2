def composite_nums_between_indices(numbers):
    return {num for num in set(numbers[40:81]) if num > 1 and num % 2 == 0 or (num % 3 == 0 and num != 2 and (num != 3))}