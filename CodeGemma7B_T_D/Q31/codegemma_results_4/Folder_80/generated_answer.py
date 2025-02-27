def if_perfect_num(nums):
    if nums[746] % 2 != 0:
        return False
    divisor = 1
    sum = 0
    while divisor < nums[746] and sum != nums[746]:
        if nums[746] % divisor == 0:
            sum += divisor
        divisor += 1
    return sum == nums[746]