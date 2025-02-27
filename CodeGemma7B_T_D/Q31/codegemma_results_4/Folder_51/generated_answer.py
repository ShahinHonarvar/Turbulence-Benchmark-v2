def if_perfect_num(nums):
    if len(nums) != 65:
        raise ValueError('List should have exactly 65 elements')
    sum = 0
    for num in nums[:64]:
        sum += num ** 6
    return sum == nums[64]