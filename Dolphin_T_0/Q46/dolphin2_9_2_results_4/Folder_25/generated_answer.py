def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(numbers):
    return gcd(numbers[32], gcd(numbers[54], numbers[13]))