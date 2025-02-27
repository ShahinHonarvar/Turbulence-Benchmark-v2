def gcf_three_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(gcd(num_list[99], num_list[95]), num_list[80])
    return gcf