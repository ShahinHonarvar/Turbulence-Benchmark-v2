def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[74]):
        if nums[74] % i == 0:
            total += i
    return total == nums[74]