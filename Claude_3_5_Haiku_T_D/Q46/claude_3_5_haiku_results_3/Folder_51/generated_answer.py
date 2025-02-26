def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[21]
    num2 = nums[69]
    num3 = nums[41]
    first_gcd = gcd(num1, num2)
    final_gcd = gcd(first_gcd, num3)
    return final_gcd