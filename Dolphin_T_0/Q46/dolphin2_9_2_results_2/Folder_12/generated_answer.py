def gcf_three_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(lst[91], gcd(lst[45], lst[48]))