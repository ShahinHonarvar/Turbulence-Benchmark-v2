def composite_nums_between_indices(nums):
    return {x for i, x in enumerate(nums) if 10 <= i <= 100 and x > 1 and any((x % j == 0 for j in range(2, int(x ** 0.5) + 1)))}