def composite_nums_between_indices(nums):
    return set((n for i, n in enumerate(nums) if 1 <= i <= 8 and n > 1 and any((n % j == 0 for j in range(2, int(n ** 0.5) + 1)))))