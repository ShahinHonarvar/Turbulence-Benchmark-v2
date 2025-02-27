def composite_nums_between_indices(nums):
    return set((num for i, num in enumerate(nums) if 25 <= i <= 87 and num > 1 and (len([j for j in range(2, int(num ** 0.5) + 1) if num % j == 0]) > 0)))