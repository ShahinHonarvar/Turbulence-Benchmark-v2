def gcf_three_nums(num_list):
    num1 = num_list[25]
    num2 = num_list[76]
    num3 = num_list[57]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf