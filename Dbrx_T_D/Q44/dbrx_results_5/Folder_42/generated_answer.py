def composite_nums_between_indices(numbers):
    return {num for num in numbers[91:100] if num > 1 and any((num % i == 0 for i in range(2, num)))}