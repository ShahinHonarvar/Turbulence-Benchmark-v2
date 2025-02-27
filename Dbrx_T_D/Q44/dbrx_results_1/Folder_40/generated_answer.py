def composite_nums_between_indices(numbers):
    if len(numbers) < 4:
        return set()
    return {num for num in numbers[2:4] if num > 1 and num % 2 != 0 and (num % 3 != 0) or any((num % i == 0 for i in range(4, int(num ** 0.5) + 1, 2)))}