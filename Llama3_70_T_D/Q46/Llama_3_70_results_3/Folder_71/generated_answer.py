def gcf_three_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(lst[24], gcd(lst[45], lst[38]))