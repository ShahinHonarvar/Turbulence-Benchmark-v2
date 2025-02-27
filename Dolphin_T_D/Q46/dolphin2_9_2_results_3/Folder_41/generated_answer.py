def gcf_three_nums(nums_list):
    num1 = nums_list[19]
    num2 = nums_list[94]
    num3 = nums_list[78]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)