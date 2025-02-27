def gcf_two_nums(lst):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(lst[618], lst[195])