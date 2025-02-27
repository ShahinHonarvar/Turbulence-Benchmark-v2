def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if 80 < len(lst) or 25 < len(lst):
        return gcd(lst[25], lst[80])
    else:
        return None