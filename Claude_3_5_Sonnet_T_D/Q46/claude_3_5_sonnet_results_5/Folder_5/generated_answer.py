def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(num_list) < 81:
        return None
    num1, num2, num3 = (num_list[64], num_list[80], num_list[15])
    gcf = gcd(gcd(num1, num2), num3)
    return gcf