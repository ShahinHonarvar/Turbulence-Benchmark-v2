def composite_nums_between_indices(numbers):
    if len(numbers) < 3:
        return set()
    return {num for num in numbers[2:4] if num > 1 and num % 2 == 0 or num % 3 == 0 or (num % 5 == 0 and num != 2 and (num != 3) and (num != 5))}