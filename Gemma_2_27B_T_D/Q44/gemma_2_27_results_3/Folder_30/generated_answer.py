def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 19 <= i <= 92 and num > 1 and all((num % j for j in range(2, int(num ** 0.5) + 1)))}