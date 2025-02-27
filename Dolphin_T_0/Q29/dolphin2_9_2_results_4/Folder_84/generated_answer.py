def gcf_two_nums(lst):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    if len(lst) < 722:
        return None
    else:
        return gcd(lst[360], lst[722])