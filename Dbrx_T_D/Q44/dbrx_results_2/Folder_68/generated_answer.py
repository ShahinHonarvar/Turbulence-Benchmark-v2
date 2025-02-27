def composite_nums_between_indices(numbers):
    if len(numbers) < 9:
        return set()
    return {num for num in numbers[0:9] if num > 1 and (not any((num % div == 0 for div in range(2, num))))}