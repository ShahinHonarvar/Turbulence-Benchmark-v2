def gcf_three_nums(num_list):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(num_list[20], gcd(num_list[17], num_list[28]))