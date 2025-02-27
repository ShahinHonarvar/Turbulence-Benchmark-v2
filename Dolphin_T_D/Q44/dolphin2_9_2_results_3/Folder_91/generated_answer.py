def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if 5 <= i <= 5 and all((n % j != 0 for j in range(2, int(n ** 0.5) + 1)))}