def gcf_three_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = num_list[558]
    num2 = num_list[110]
    num3 = num_list[628]
    return gcd(gcd(num1, num2), num3)