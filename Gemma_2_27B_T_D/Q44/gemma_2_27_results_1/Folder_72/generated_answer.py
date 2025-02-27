def composite_nums_between_indices(nums):
    return {num for idx, num in enumerate(nums) if 55 <= idx <= 98 and num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}