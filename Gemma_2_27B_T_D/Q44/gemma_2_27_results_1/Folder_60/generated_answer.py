def composite_nums_between_indices(nums):
    return {x for i, x in enumerate(nums) if 29 <= i <= 51 and x > 1 and any((x % j == 0 for j in range(2, int(x ** 0.5) + 1)))}