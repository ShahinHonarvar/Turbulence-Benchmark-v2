def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if 56 <= i <= 82 and n > 1 and any((n % j == 0 for j in range(2, int(n ** 0.5) + 1)))}