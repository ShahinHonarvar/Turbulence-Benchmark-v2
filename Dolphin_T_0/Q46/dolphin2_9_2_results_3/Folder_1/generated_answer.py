def gcf_three_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcd = gcf(num_list[74], num_list[51])
    gcd = gcf(gcd, num_list[27])
    return gcd