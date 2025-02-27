def composite_nums_between_indices(numbers):
    return set((num for i, num in enumerate(numbers) if 686 <= i <= 987 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))))