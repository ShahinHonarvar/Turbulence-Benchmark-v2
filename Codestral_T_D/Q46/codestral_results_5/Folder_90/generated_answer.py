def gcf_three_nums(num_list):
    num1 = num_list[818]
    num2 = num_list[606]
    num3 = num_list[873]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)