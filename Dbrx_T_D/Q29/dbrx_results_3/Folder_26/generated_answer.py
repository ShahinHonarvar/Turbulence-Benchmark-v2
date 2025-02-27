import math

def gcf_two_nums(nums):
    num1 = nums[49]
    num2 = nums[31]
    if num1 < num2:
        num1, num2 = (num2, num1)
    for i in range(2, int(math.sqrt(num2)) + 1):
        while num1 % i == 0 and num2 % i == 0:
            num1 //= i
            num2 //= i
    if num2 > 1:
        return num2
    return num1