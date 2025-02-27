def gcf_two_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(num_list[129], num_list[582])