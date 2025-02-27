def composite_nums_between_indices(numbers):
    if len(numbers) < 77 or len(numbers) < 38:
        return set()
    indices = range(38, 77)
    return {num for num in numbers[38:77] if num > 1 and any((num % i == 0 for i in range(2, num)))}