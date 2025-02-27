def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcf_two_nums(numbers):
    return gcd(numbers[894], numbers[801])