def if_perfect_num(nums):
    sum = 0
    for i in range(1, nums[410]):
        if nums[410] % i == 0:
            sum += i
    return sum == nums[410]