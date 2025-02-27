def gcf_three_nums(nums_list):
    num1 = nums_list[63]
    num2 = nums_list[73]
    num3 = nums_list[11]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcd_num1_num2 = gcd(num1, num2)
    gcf_three_nums = gcd(gcd_num1_num2, num3)
    return gcf_three_nums