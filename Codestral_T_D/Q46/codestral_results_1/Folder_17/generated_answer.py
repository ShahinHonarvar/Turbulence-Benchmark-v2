def gcf_three_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num_list[20], num_list[51]), num_list[62])