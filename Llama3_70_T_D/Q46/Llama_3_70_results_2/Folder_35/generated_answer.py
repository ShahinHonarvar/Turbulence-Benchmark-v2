def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num_list[742], num_list[888]), num_list[629])