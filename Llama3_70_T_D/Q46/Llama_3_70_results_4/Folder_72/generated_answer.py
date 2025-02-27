def gcf_three_nums(num_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = num_list[44]
    b = num_list[91]
    c = num_list[42]
    return gcd(gcd(a, b), c)