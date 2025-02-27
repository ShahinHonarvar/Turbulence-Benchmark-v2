def composite_nums_between_indices(numbers):
    start, end = (4, 4 + 4)
    composites = {num for num in numbers[start:end + 1] if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}
    return composites