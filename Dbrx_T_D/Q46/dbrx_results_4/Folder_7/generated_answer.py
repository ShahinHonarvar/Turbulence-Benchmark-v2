def gcf_three_nums(nums):
    num1 = nums[477]
    num2 = nums[696]
    num3 = nums[663]

    def gcd(num1, num2):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    num1_gcd = gcd(num1, num3)
    num2_gcd = gcd(num1_gcd, num2)
    num1_lcm = num1 * num2 // num2_gcd
    num3_lcm = num1_lcm * num3 // gcd(num1_lcm, num3)
    return gcd(num1_lcm, num3_lcm) if num3_lcm % num1_lcm == 0 else 1