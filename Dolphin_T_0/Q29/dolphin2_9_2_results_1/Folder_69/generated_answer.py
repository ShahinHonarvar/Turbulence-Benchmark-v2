def gcf_two_nums(num_list):

    def gcd(a, b):
        if b:
            return gcd(b, a % b)
        else:
            return a
    return gcd(num_list[894], num_list[801])