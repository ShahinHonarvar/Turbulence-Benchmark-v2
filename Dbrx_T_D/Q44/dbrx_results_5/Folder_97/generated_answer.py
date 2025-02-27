def composite_nums_between_indices(numbers):
    if len(numbers) < 40:
        return set()
    return {num for num in numbers[15:40] if num > 1 and num % 2 == 0 and ((num - 1) % 3 == 0)}