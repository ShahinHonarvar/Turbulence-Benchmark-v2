def composite_nums_between_indices(numbers):
    return {num for num in set(numbers[25:60]) if num > 1 and (not all((num % i == 0 for i in range(2, num))))}