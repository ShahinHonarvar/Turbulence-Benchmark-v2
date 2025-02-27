def if_perfect_num(nums):
    total = 0
    for i in range(1, nums[459]):
        if nums[459] % i == 0:
            total += i
    return total == nums[459]