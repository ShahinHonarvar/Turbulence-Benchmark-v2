def composite_nums_between_indices(nums):
    return set((n for i, n in enumerate(nums) if 22 <= i <= 88 and n > 1 and any((n % i == 0 for i in range(2, int(n ** 0.5) + 1)))))