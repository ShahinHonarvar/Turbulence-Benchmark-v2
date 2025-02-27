def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[41]
    num2 = num_list[69]
    num3 = num_list[28]
    gcf = gcd(num1, num2)
    return gcd(gcf, num3)