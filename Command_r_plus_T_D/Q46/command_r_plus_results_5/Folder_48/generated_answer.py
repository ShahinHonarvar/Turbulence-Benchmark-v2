def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[653]
    num2 = num_list[311]
    num3 = num_list[440]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf