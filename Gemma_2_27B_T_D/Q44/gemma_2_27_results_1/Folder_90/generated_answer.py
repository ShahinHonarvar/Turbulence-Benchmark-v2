def composite_nums_between_indices(nums):
    return {x for i, x in enumerate(nums) if 333 <= i <= 368 and x > 1 and (sum((1 for j in range(2, int(x ** 0.5) + 1) if x % j == 0)) >= 1)}