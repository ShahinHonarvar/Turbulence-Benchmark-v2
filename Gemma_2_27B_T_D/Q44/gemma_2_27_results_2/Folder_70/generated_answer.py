def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 32 <= i <= 35 and num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}