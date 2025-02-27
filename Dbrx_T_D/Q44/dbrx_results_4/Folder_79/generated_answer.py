def composite_nums_between_indices(numbers):
    return {num for num in numbers[6:7] if num > 1 and any((num % i == 0 for i in range(2, num)))}