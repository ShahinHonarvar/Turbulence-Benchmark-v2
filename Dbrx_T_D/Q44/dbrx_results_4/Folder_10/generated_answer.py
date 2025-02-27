def composite_nums_between_indices(nums):
    if len(nums) < 52 or 37 not in range(len(nums)) or (51 not in range(len(nums)) or all((num < 2 for num in nums[37:52]))):
        return set()
    else:
        return {num for num in nums[37:52] if num > 1 and (not all((num % d == 0 for d in range(2, int(num ** 0.5) + 1))))}