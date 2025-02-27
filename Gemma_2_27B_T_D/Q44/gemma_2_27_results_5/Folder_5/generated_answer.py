def composite_nums_between_indices(nums):
    return set((num for i, num in enumerate(nums) if 1 <= i <= 5 and num > 1 and any((num % j == 0 for j in range(2, int(num ** 0.5) + 1)))))