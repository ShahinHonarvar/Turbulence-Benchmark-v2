def composite_nums_between_indices(nums):
    return {num for num in set(nums[i]) for i in range(64, 67) if num > 1 and num % 2 == 0 and all((num % j != 0 for j in range(3, int(num ** 0.5) + 1)))}