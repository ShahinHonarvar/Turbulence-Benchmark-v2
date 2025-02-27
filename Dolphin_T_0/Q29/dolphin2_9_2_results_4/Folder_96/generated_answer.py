def gcf_two_nums(int_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(int_list[95], int_list[73])