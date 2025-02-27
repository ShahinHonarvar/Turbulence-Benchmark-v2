def gcf_two_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    if len(lst) < 94:
        return None
    else:
        return gcd(lst[78], lst[93])