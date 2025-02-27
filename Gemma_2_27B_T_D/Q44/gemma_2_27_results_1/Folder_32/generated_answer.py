def composite_nums_between_indices(nums):
    return {x for i, x in enumerate(nums) if 10 <= i <= 66 and x > 1 and all((x % j for j in range(2, int(x ** 0.5) + 1)))}