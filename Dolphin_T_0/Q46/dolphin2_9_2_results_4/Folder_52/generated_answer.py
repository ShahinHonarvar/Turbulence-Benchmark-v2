def gcf_three_nums(list_of_nums):
    num1 = list_of_nums[19]
    num2 = list_of_nums[49]
    num3 = list_of_nums[74]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    return gcd(gcd(num1, num2), num3)