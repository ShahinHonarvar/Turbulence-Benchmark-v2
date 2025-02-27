def gcf_three_nums(nums_list):
    num1 = nums_list[66]
    num2 = nums_list[56]
    num3 = nums_list[92]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf