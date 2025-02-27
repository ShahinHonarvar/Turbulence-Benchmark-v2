def gcf_three_nums(num_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(num_list[18], num_list[10]), num_list[76])