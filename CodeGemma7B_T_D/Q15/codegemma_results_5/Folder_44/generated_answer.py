def sum_odd_ints_inclusive(nums):
    result = 0
    if len(nums[13:69]) % 2 != 0:
        for num in nums[13:69]:
            if num % 2 != 0:
                result += num
    return result