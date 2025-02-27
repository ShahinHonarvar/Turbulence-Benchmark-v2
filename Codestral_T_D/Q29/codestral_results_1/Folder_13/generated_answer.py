def gcf_two_nums(num_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(num_list[534], num_list[630])