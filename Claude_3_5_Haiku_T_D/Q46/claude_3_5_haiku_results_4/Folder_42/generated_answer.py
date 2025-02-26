def gcf_three_nums(nums_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums_list[19]
    num2 = nums_list[69]
    num3 = nums_list[97]
    result = gcd(num1, gcd(num2, num3))
    return result