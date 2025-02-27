def composite_nums_between_indices(numbers):
    return set((num for num in numbers[29:52] if num > 1 and (not all((num % i for i in range(2, num))))))