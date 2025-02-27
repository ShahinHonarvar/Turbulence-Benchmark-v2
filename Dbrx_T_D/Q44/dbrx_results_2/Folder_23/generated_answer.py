def composite_nums_between_indices(nums):
    return {num for num in nums[20:31] if not num < 2 or (num % 2 == 0 and num > 2) or any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}