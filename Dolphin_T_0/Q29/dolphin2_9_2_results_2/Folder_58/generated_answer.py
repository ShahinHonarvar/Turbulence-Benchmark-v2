def gcf_two_nums(lst):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    if 129 < len(lst) and 582 < len(lst):
        return gcd(lst[129], lst[582])
    else:
        raise IndexError('Indices out of range')