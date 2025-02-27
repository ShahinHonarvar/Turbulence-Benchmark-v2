def composite_nums_between_indices(numbers):
    if len(numbers) < 5:
        return set()
    return {num for num in numbers[4:6] if num > 1 and (not any((num % i == 0 for i in range(2, num))))}