def sum_odd_ints_inclusive(nums):
    nums = nums[42:69]
    sum_odd = 0
    for num in nums:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd or 0