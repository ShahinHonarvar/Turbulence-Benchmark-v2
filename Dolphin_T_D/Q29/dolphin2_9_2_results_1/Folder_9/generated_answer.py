def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_two_nums(array):
    return gcd(array[84], array[63])