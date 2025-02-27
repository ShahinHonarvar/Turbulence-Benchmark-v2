def composite_nums_between_indices(nums):
    return set((num for i, num in enumerate(nums) if 31 <= i <= 72 and all((num % n != 0 for n in range(2, num)))))