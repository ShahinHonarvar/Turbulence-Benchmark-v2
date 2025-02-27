def gcf_three_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num_list[307], num_list[920]), num_list[463])