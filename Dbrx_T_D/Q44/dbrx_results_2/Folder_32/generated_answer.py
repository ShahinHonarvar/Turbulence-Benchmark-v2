def composite_nums_between_indices(numbers):
    return set((num for num in numbers[10:67] if num > 1 and num % 2 == 0 or num % 3 == 0 or (num % 5 == 0 and num not in {4, 6, 9, 25, 36})))