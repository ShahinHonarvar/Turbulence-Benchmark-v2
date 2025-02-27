def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(gcd(num_list[20], num_list[51]), num_list[62])
    return gcf