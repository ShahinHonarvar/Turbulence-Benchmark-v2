def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[944]
    num2 = nums[814]
    num3 = nums[865]
    gcf_1_2 = gcd(num1, num2)
    return gcd(gcf_1_2, num3)