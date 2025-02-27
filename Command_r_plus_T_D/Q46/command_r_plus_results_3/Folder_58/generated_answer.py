def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[144]
    num2 = num_list[182]
    num3 = num_list[769]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf