def gcf_three_nums(nums):
    num1 = nums[59]
    num2 = nums[93]
    num3 = nums[84]
    factors = list(set(range(1, min(num1, num2, num3))) & set(list(filter(lambda x: num1 % x == 0 and num2 % x == 0 and (num3 % x == 0), range(1, min(num1, num2, num3))))))
    return max(factors)