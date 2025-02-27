def composite_nums_between_indices(numbers):
    return {num for num in numbers[43:87] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))}