def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_of_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf_of_three(num_list[56], num_list[88], num_list[51])