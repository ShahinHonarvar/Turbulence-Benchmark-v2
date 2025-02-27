from functools import reduce

def gcf_three_nums(numbers):
    nums = [numbers[49], numbers[46], numbers[13]]

    def gcd(num1, num2):
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1

    def gcf(num1, num2, num3):
        return gcd(gcd(num1, num2), num3)
    return gcf(nums[0], nums[1], nums[2])