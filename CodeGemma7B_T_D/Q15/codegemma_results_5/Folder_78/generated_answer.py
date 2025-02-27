def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    filtered_nums = [num for num in nums[43:52] if num % 2 != 0]
    return sum(filtered_nums) if filtered_nums else 0