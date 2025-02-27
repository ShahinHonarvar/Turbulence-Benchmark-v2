def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if i >= 43 and i <= 86 and (n > 1) and all((n % j for j in range(2, int(n ** 0.5) + 1)))}