def gcf_three_nums(num_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = num_list[99]
    num2 = num_list[95]
    num3 = num_list[80]
    return gcd(gcd(num1, num2), num3)