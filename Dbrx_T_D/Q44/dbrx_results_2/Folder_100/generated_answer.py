def composite_nums_between_indices(numbers):
    if len(numbers) < 93:
        return set()
    composite_numbers = set((num for num in numbers[12:93] if num > 1 and (not num & 1) and (not num % 3) or (num > 4 and num % 2 == 0 and all((num % i != 0 for i in range(5, int(num ** 0.5) + 1))))))
    return composite_numbers