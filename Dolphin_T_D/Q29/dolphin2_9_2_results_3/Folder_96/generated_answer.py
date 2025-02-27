def gcf_two_nums(lst):

    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return gcd(a - b, b)
        return gcd(a, b - a)
    return gcd(lst[95], lst[73])