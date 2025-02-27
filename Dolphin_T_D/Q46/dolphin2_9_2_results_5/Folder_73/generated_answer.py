def gcf_three_nums(num_list):
    num1 = num_list[90]
    num2 = num_list[84]
    num3 = num_list[47]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcd(num1, num2)
    result = gcd(result, num3)
    return result